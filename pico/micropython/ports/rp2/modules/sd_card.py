# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
#
# Copyright (c) 2022 DC540 Defcon Group
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

from micropython import const
import time


class SDCard:
    """
    Class to handle SDCard functionality
    """

    # sd card registers & commands
    START_BLOCK_TOKEN = const(0xfc)
    STOP_TRAN_TOKEN = const(0xfd)
    START_BLOCK = const(0xfe)
    CMD_TIMEOUT = const(100)
    R1_IDLE_STATE = const(1 << 0)
    R1_ILLEGAL_COMMAND = const(1 << 2)

    def __init__(self, spi, cs):
        """
        Params:
            spi: object
            cs: object
            baudrate: int, optional
        """
        self.spi = spi
        self.cs = cs
        self.cmdbuf = bytearray(6)
        self.dummybuf = bytearray(512)
        self.tokenbuf = bytearray(1)
        for i in range(512):
            self.dummybuf[i] = 0xFF
        self.dummybuf_memoryview = memoryview(self.dummybuf)
        # initialise the card
        self.__init_card()

    def __init_card(self):
        """
        Private method to handle init of sd card
        """
        # init CS pin
        self.cs.init(self.cs.OUT, value=1)
        # clock card at least 100 cycles with cs high
        for i in range(16):
            self.spi.write(b'\xff')
        # CMD0: init card should return R1_IDLE_STATE (allow 5 attempts)
        for _ in range(5):
            if self.__write_cmd(0, 0, 0x95) == self.R1_IDLE_STATE:
                break
        else:
            raise OSError('no SD card')
        # CMD8: determine card version
        r = self.__write_cmd(8, 0x01AA, 0x87, 4)
        if r == self.R1_IDLE_STATE:
            self.__init_card_v2()
        elif r == (self.R1_IDLE_STATE | self.R1_ILLEGAL_COMMAND):
            self.__init_card_v1()
        else:
            raise OSError('could not determine SD card version')
        # get the number of sectors
        # CMD9: response R2 (R1 byte + 16-byte block read)
        if self.__write_cmd(9, 0, 0, 0, False) != 0:
            raise OSError('no response from SD card')
        csd = bytearray(16)
        self.__read_cmd(csd)
        if csd[0] & 0xC0 == 0x40:  # CSD version 2.0
            self.sectors = ((csd[8] << 8 | csd[9]) + 1) * 1024
        elif csd[0] & 0xC0 == 0x00:  # CSD version 1.0 (old, <= 2GB)
            c_size = csd[6] & 0b11 | csd[7] << 2 | (csd[8] & 0b11000000) << 4
            c_size_mult = ((csd[9] & 0b11) << 1) | csd[10] >> 7
            self.sectors = (c_size + 1) * (2 ** (c_size_mult + 2))  # noqa
        else:
            raise OSError('SD card CSD format not supported')
        # CMD16: set block length to 512 bytes
        if self.__write_cmd(16, 512, 0) != 0:
            raise OSError('cannot set 512 block size')

    def __init_card_v1(self):
        """
        Private method to handle init card version 1
        """
        for i in range(self.CMD_TIMEOUT):
            self.__write_cmd(55, 0, 0)
            if self.__write_cmd(41, 0, 0) == 0:
                self.cdv = 512
                return
        # raise OSError('timeout waiting for v1 card')

    def __init_card_v2(self):
        """
        Private method to handle init card version 2
        """
        for i in range(self.CMD_TIMEOUT):
            time.sleep_ms(50)
            self.__write_cmd(58, 0, 0, 4)
            self.__write_cmd(55, 0, 0)
            if self.__write_cmd(41, 0x40000000, 0) == 0:
                self.__write_cmd(58, 0, 0, 4)
                self.cdv = 1  # noqa
                return
        raise OSError('timeout waiting for v2 card')

    def __write_cmd(self, cmd, arg, crc, final=0, release=True, skip1=False):
        """
        Private method to handle write command

        Params:
            cmd: int
            arg: int
            crc: int
            final: int, optional
            release: bool, optional
            skip1: bool, optional

        Returns:
            int
        """
        self.cs(0)
        # create and send the command
        buf = self.cmdbuf
        buf[0] = 0x40 | cmd
        buf[1] = arg >> 24
        buf[2] = arg >> 16
        buf[3] = arg >> 8
        buf[4] = arg
        buf[5] = crc
        self.spi.write(buf)
        if skip1:
            self.spi.readinto(self.tokenbuf, 0xFF)
        # wait for the response (response[7] == 0)
        for i in range(self.CMD_TIMEOUT):
            self.spi.readinto(self.tokenbuf, 0xFF)
            response = self.tokenbuf[0]
            if not (response & 0x80):
                # this could be a big-endian integer that we are getting here
                for j in range(final):
                    self.spi.write(b'\xff')
                if release:
                    self.cs(1)
                    self.spi.write(b'\xff')
                return response
        # timeout
        self.cs(1)
        self.spi.write(b'\xff')
        return -1

    def __read_cmd(self, buf):
        """
        Private method to handle read cmd

        Params:
            buf: int
        """
        self.cs(0)
        # read until start byte (0xff)
        for i in range(self.CMD_TIMEOUT):
            self.spi.readinto(self.tokenbuf, 0xFF)
            if self.tokenbuf[0] == self.START_BLOCK:
                break
            time.sleep_ms(1)
        else:
            self.cs(1)
            raise OSError('timeout waiting for response')
        # read data
        mv = self.dummybuf_memoryview
        if len(buf) != len(mv):
            mv = mv[: len(buf)]
        self.spi.write_readinto(mv, buf)
        # read checksum
        self.spi.write(b'\xff')
        self.spi.write(b'\xff')
        self.cs(1)
        self.spi.write(b'\xff')

    def __write(self, token, buf):
        """
        Private method to handle write operation

        Params:
            token: int
            buf: int
        """
        self.cs(0)
        # send: start of block, data, checksum
        self.spi.read(1, token)
        self.spi.write(buf)
        self.spi.write(b'\xff')
        self.spi.write(b'\xff')
        # check the response
        if (self.spi.read(1, 0xFF)[0] & 0x1F) != 0x05:
            self.cs(1)
            self.spi.write(b'\xff')
            return
        # wait for write to finish
        while self.spi.read(1, 0xFF)[0] == 0:
            pass
        self.cs(1)
        self.spi.write(b'\xff')

    def __write_token(self, token):
        """
        Private method to handle writing of a token

        Params:
            token: int
        """
        self.cs(0)
        self.spi.read(1, token)
        self.spi.write(b'\xff')
        # wait for write to finish
        while self.spi.read(1, 0xFF)[0] == 0x00:
            pass
        self.cs(1)
        self.spi.write(b'\xff')

    def readblocks(self, block_num, buf):
        """
        Method to handle reading of blocks on drive

        Params:
            block_num: list
            buf: int
        """
        nblocks = len(buf) // 512
        assert nblocks and not len(buf) % 512, 'buffer length is invalid'
        if nblocks == 1:
            # CMD17: set read address for single block
            if self.__write_cmd(17, block_num * self.cdv, 0, release=False) != 0:
                # release the card
                self.cs(1)
                raise OSError(5)  # EIO
            # receive the data and release card
            self.__read_cmd(buf)
        else:
            # CMD18: set read address for multiple blocks
            if self.__write_cmd(18, block_num * self.cdv, 0, release=False) != 0:
                # release the card
                self.cs(1)
                raise OSError(5)  # EIO
            offset = 0
            mv = memoryview(buf)
            while nblocks:
                # receive the data and release card
                self.__read_cmd(mv[offset: offset + 512])
                offset += 512
                nblocks -= 1
            if self.__write_cmd(12, 0, 0xFF, skip1=True):
                raise OSError(5)  # EIO

    def writeblocks(self, block_num, buf):
        """
        Method to handle writing of blocks on drive

        Params:
            block_num: int
            buf: int
        """
        nblocks, err = divmod(len(buf), 512)
        assert nblocks and not err, 'buffer length is invalid'
        if nblocks == 1:
            # CMD24: set write address for single block
            if self.__write_cmd(24, block_num * self.cdv, 0) != 0:
                raise OSError(5)  # EIO
            # send the data
            self.__write(self.START_BLOCK, buf)
        else:
            # CMD25: set write address for first block
            if self.__write_cmd(25, block_num * self.cdv, 0) != 0:
                raise OSError(5)  # EIO
            # send the data
            offset = 0
            mv = memoryview(buf)
            while nblocks:
                self.__write(self.START_BLOCK_TOKEN, mv[offset: offset + 512])  # noqa
                offset += 512
                nblocks -= 1
            self.__write_token(self.STOP_TRAN_TOKEN)

    def ioctl(self, op, arg):  # noqa
        """
        Method to handle input/output control functionality

        Params:
            op: int
            arg: str, optional

        Returns:
            int
        """
        # get number of blocks
        if op == 4:
            return self.sectors

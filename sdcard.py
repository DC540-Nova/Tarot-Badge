# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
# Developer: Corinne "Rinn" Neidig
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
    
    _CMD_TIMEOUT = const(100)
    _R1_IDLE_STATE = const(1 << 0)
    _R1_ILLEGAL_COMMAND = const(1 << 2)
    _TOKEN_STOP_TRAN = const(0xFD)
    _TOKEN_DATA = const(0xFE)
    
    def __init__(self, spi, cs, baudrate=1320000):
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
        self.init_card(baudrate)

    def init_spi(self, baudrate):
        """
        Method to handle init of spi device
        
        Params:
            baudrate: int
        """
        try:
            master = self.spi.MASTER
        except AttributeError:
            self.spi.init(baudrate=baudrate, phase=0, polarity=0)
        else:
            self.spi.init(master, baudrate=baudrate, phase=0, polarity=0)

    def init_card(self, baudrate):
        """
        Method to handle init of spi device
        
        Params:
            baudrate: int
        """
        self.cs.init(self.cs.OUT, value=1)
        self.init_spi(100000)
        for i in range(16):
            self.spi.write(b'\xff')
        for _ in range(5):
            if self.cmd(0, 0, 0x95) == _R1_IDLE_STATE:
                break
        else:
            raise OSError('no SD card')
        r = self.cmd(8, 0x01AA, 0x87, 4)
        if r == _R1_IDLE_STATE:
            self.init_card_v2()
        elif r == (_R1_IDLE_STATE | _R1_ILLEGAL_COMMAND):
            self.init_card_v1()
        else:
            raise OSError('could not determine SD card version')
        if self.cmd(9, 0, 0, 0, False) != 0:
            raise OSError('no response from SD card')
        csd = bytearray(16)
        self.readinto(csd)
        if csd[0] & 0xC0 == 0x40: 
            self.sectors = ((csd[8] << 8 | csd[9]) + 1) * 1024
        elif csd[0] & 0xC0 == 0x00:
            c_size = csd[6] & 0b11 | csd[7] << 2 | (csd[8] & 0b11000000) << 4
            c_size_mult = ((csd[9] & 0b11) << 1) | csd[10] >> 7
            self.sectors = (c_size + 1) * (2 ** (c_size_mult + 2))
        else:
            raise OSError('SD card CSD format not supported')
        if self.cmd(16, 512, 0) != 0:
            raise OSError('cannot set 512 block size')
        self.init_spi(baudrate)

    def init_card_v1(self):
        """
        Method to handle init card version 1
        """
        for i in range(_CMD_TIMEOUT):
            self.cmd(55, 0, 0)
            if self.cmd(41, 0, 0) == 0:
                self.cdv = 512
                return
        raise OSError('timeout waiting for v1 card')

    def init_card_v2(self):
        """
        Method to handle init card version 1
        """
        for i in range(_CMD_TIMEOUT):
            time.sleep_ms(50)
            self.cmd(58, 0, 0, 4)
            self.cmd(55, 0, 0)
            if self.cmd(41, 0x40000000, 0) == 0:
                self.cmd(58, 0, 0, 4)
                self.cdv = 1
                return
        raise OSError('timeout waiting for v2 card')

    def cmd(self, cmd, arg, crc, final=0, release=True, skip1=False):
        """
        Method to handle cmd functionality
        
        Params:
            cmd: int
            arg: int
            crc: int
            final: int, optional
            release: bool, optional
            skip1: bool, optional
        """
        self.cs(0)
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
        for i in range(_CMD_TIMEOUT):
            self.spi.readinto(self.tokenbuf, 0xFF)
            response = self.tokenbuf[0]
            if not (response & 0x80):
                for j in range(final):
                    self.spi.write(b'\xff')
                if release:
                    self.cs(1)
                    self.spi.write(b'\xff')
                return response
        self.cs(1)
        self.spi.write(b'\xff')
        return -1

    def readinto(self, buf):
        """
        Method to handle reading info
        
        Params:
            buf: int
        """
        self.cs(0)
        for i in range(_CMD_TIMEOUT):
            self.spi.readinto(self.tokenbuf, 0xFF)
            if self.tokenbuf[0] == _TOKEN_DATA:
                break
            time.sleep_ms(1)
        else:
            self.cs(1)
            raise OSError('timeout waiting for response')
        mv = self.dummybuf_memoryview
        if len(buf) != len(mv):
            mv = mv[: len(buf)]
        self.spi.write_readinto(mv, buf)
        self.spi.write(b'\xff')
        self.spi.write(b'\xff')
        self.cs(1)
        self.spi.write(b'\xff')

    def write(self, token, buf):
        """
        Method to handle write operation
        
        Params:
            token: int
            buf: int
        """
        self.cs(0)
        self.spi.read(1, token)
        self.spi.write(buf)
        self.spi.write(b'\xff')
        self.spi.write(b'\xff')
        if (self.spi.read(1, 0xFF)[0] & 0x1F) != 0x05:
            self.cs(1)
            self.spi.write(b'\xff')
            return
        while self.spi.read(1, 0xFF)[0] == 0:
            pass
        self.cs(1)
        self.spi.write(b'\xff')

    def write_token(self, token):
        """
        Method to handle writing of token
        
        Params:
            token: int
        """
        self.cs(0)
        self.spi.read(1, token)
        self.spi.write(b'\xff')
        while self.spi.read(1, 0xFF)[0] == 0x00:
            pass
        self.cs(1)
        self.spi.write(b'\xff')

    def readblocks(self, block_num, buf):
        """
        Method to handle reading of blocks on drive
        
        Params:
            block_num: int
            buf: int
        """
        nblocks = len(buf) // 512
        assert nblocks and not len(buf) % 512, 'buffer length is invalid'
        if nblocks == 1:
            if self.cmd(17, block_num * self.cdv, 0, release=False) != 0:
                self.cs(1)
                raise OSError(5)
            self.readinto(buf)
        else:
            if self.cmd(18, block_num * self.cdv, 0, release=False) != 0:
                self.cs(1)
                raise OSError(5) 
            offset = 0
            mv = memoryview(buf)
            while nblocks:
                self.readinto(mv[offset : offset + 512])
                offset += 512
                nblocks -= 1
            if self.cmd(12, 0, 0xFF, skip1=True):
                raise OSError(5) 

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
            if self.cmd(24, block_num * self.cdv, 0) != 0:
                raise OSError(5)
            self.write(_TOKEN_DATA, buf)
        else:
            if self.cmd(25, block_num * self.cdv, 0) != 0:
                raise OSError(5) 
            offset = 0
            mv = memoryview(buf)
            while nblocks:
                self.write(_TOKEN_CMD25, mv[offset : offset + 512])
                offset += 512
                nblocks -= 1
            self.write_token(_TOKEN_STOP_TRAN)

    def ioctl(self, op, arg):
        """
        Method to handle ioctl functionality
        
        Params:
            opm: int
            arg: int
            
        Returns:
            int
        """
        if op == 4: 
            return self.sectors
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

import utime
from micropython import const


class NRF:
    """
    Class to handle NRF driver
    """

    # nRF24l01 registers & commands
    CONFIG = const(0x00)
    EN_AA = const(0x01)
    EN_RXADDR = const(0x02)
    SETUP_AW = const(0x03)
    SETUP_RETR = const(0x04)
    RF_CH = const(0x05)
    RF_SETUP = const(0x06)
    STATUS = const(0x07)
    OBSERVE_TX = const(0x08)
    RPD = const(0x09)
    RX_ADDR_P0 = const(0x0a)
    RX_ADDR_P1 = const(0x0b)
    RX_ADDR_P2 = const(0x0c)
    RX_ADDR_P3 = const(0x0d)
    RX_ADDR_P4 = const(0x0e)
    RX_ADDR_P5 = const(0x0f)
    TX_ADDR = const(0x10)
    RX_PW_P0 = const(0x11)
    RX_PW_P1 = const(0x12)
    RX_PW_P2 = const(0x13)
    RX_PW_P3 = const(0x14)
    RX_PW_P4 = const(0x15)
    RX_PW_P5 = const(0x16)
    FIFO_STATUS = const(0x17)
    DYNPD = const(0x1c)
    FEATURE = const(0x1d)
    R_REGISTER = const(0b00011111)
    W_REGISTER = const(0b00111111)
    R_RX_PAYLOAD = const(0b01100001)
    W_TX_PAYLOAD = const(0b10100000)
    FLUSH_TX = const(0b11100001)
    FLUSH_RX = const(0b11100010)
    REUSE_TX_PL = const(0b11100011)
    R_RX_PL_WID = const(0b01100000)
    W_ACK_PAYLOAD = const(0b10101111)
    W_TX_PAYLOAD_NO_ACK = const(0b10110000)
    NOP = const(0b11111111)

    def __init__(self, spi_conf, csn, ce):
        """
        Params:
            nrf_spi: object
            csn: object
            ce: object
        """
        utime.sleep_ms(11)
        self.ce = ce
        self.csn = csn
        self.spi = spi_conf
        self.ce(0)
        self.csn(1)
        self.__config()

    def __config(self):
        """
        Private method to handle config
        """
        self.csn(1)
        self.ce(0)
        utime.sleep_ms(11)
        self.__write_reg(self.CONFIG, 0b00001010)  # PWR_UP & EN_CRC
        utime.sleep_ms(1500)
        self.__write_reg(self.EN_AA, 0b00000011)  # ENAA_P0 & ENAA_P1
        self.__write_reg(self.SETUP_AW, 0b00000011)  # 11 = 5 bytes
        self.__write_reg(self.RF_CH, 60)  # RF channel 60
        self.__write_reg(self.RF_SETUP, 0b00001111)  #
        self.__write_reg(self.RX_ADDR_P0, "DC540")  # channel name
        self.__write_reg(self.TX_ADDR, "DC540")  # transmit address
        self.__write_reg(self.RX_PW_P0, 32)  # number of bytes in RX payload in data pipe 0
        self.recv()

    def __read_reg(self, reg, size=1, debug=False):
        """
        Private method to read a register

        Params:
            reg: int
            size: int, optional
            debug: bool, optional

        Returns:
            object
        """
        reg = [0b00011111 & reg]  # R_REGISTER command mask
        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(size)
        self.csn(1)
        if debug:
            print([bin(value) for value in result])
        return result

    def __write_reg(self, reg, value):
        """
        Private method to write to a register

        Params:
            reg: int
            size: int, optional
        """
        reg = [0b00100000 | (0b00011111 & reg)]  # W_REGISTER command mask
        value = [value] if type(value) == type(1) else value  # make sure value is a list type  # noqa
        self.csn(0)
        self.spi.write(bytearray(reg))
        self.spi.write(bytearray(value))
        self.csn(1)

    def __mode_tx(self):
        """
        Private method to enable transmit mode
        """
        config = self.__read_reg(self.CONFIG)[0]
        config &= ~(1 << 0)
        self.__write_reg(self.CONFIG, config)
        self.ce(0)
        utime.sleep_us(130)

    def __mode_rx(self):
        """
        Private method to enable receive mode
        """
        config = self.__read_reg(self.CONFIG)[0]
        config |= (1 << 0)
        self.__write_reg(self.CONFIG, config)
        self.ce(1)
        utime.sleep_us(130)

    def __send_msg(self, msg):
        """
        Private method to send a raw message

        Params:
            msg: str
        """
        self.csn(0)
        self.spi.write(bytearray([self.FLUSH_TX]))
        self.csn(1)
        status = self.__read_reg(self.STATUS)[0]
        status |= (1 << 4)
        self.__write_reg(self.STATUS, status)
        data = bytearray(msg)
        data.extend(bytearray(32 - len(msg)))
        reg = [self.W_TX_PAYLOAD]
        self.csn(0)
        self.spi.write(bytearray(reg))
        self.spi.write(bytearray(data))
        self.csn(1)
        self.ce(1)
        utime.sleep_us(10)
        self.ce(0)
        status = self.__read_reg(self.STATUS)[0]
        while (status & (1 << 5)) == 0 and (status & (1 << 4)) == 0:
            status = self.__read_reg(self.STATUS)[0]
            utime.sleep(1)
        status |= (1 << 4) | (1 << 5)
        self.__write_reg(self.STATUS, status)
        self.__mode_rx()

    def __new_msg(self):
        """
        Private method to check if there is a new message in the recieve queue

        Returns:
            bool
        """
        status = self.__read_reg(self.STATUS)[0]  # 6
        fstatus = self.__read_reg(self.FIFO_STATUS)[0]  # 1
        has_new_message = (not (0b00000001 & fstatus)) or (0b01000000 & status)
        status |= (1 << 4) | (1 << 5)
        self.__write_reg(self.STATUS, status)
        return has_new_message

    def __read_msg(self):
        """
        Private method to read a raw message

        Returns:
            bool
        """
        reg = [self.R_RX_PAYLOAD]
        self.csn(0)
        self.spi.write(bytearray(reg))
        msg = self.spi.read(32)
        self.csn(1)
        status = self.__read_reg(self.STATUS)[0]
        status |= (1 << 6)
        self.__write_reg(self.STATUS, status)
        return msg

    def recv(self):
        """
        Method to receive a mssage

        Returns:
            str
        """
        for _ in range(1):
            self.__mode_rx()
            if self.__new_msg() > 0:
                # print("".join([chr(i) for i in self.__read_msg()]))
                return "".join([chr(i) for i in self.__read_msg()])
            utime.sleep(0.001)

    def send(self, msg):
        """
        Method to send a message

        Params:
            msg: str
        """
        for _ in range(1):
            self.__mode_tx()
            self.__send_msg(msg)
            utime.sleep(0.001)

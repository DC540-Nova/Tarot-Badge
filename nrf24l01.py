# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
# Developer: Corinne "Rinn" Neidig
#
# Copyright (c) 2021 DC540 Defcon Group
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


class NRF:
    """
    Class to handle NRF driver
    """
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
        self.__write_reg(0, 0b00001010)
        utime.sleep_ms(2)
        # print(bin(self.__read_reg(0)[0]))
        utime.sleep_ms(2000)
        self.__write_reg(1, 0b00000011)
        self.__write_reg(3, 0b00000011)
        self.__write_reg(5, 60)
        self.__write_reg(6, 0b00001111)
        self.__write_reg(0x0a, "DC540")
        self.__write_reg(0x10, "DC540")
        self.__write_reg(0x11, 32)

    def __read_reg(self, reg, size=1):
        """
        Private method to read a register

        Params:
            reg: int
            size: int, optional

        Returns:
            object
        """
        reg = [0b00011111 & reg]
        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(size)
        self.csn(1)
        return result

    def __write_reg(self, reg, value):
        """
        Private method to write to a register

        Params:
            reg: int
            size: int, optional
        """
        reg = [0b00100000 | (0b00011111 & reg)]
        value = [value] if type(value) == type(1) else value  # noqa
        self.csn(0)
        self.spi.write(bytearray(reg))
        self.spi.write(bytearray(value))
        self.csn(1)



    def modeTX(self):
        config = self.__read_reg(0)[0]
        config &= ~(1 << 0)
        self.__write_reg(0, config)
        self.ce(0)
        utime.sleep_us(130)

    def modeRX(self):
        config = self.__read_reg(0)[0]
        config |= (1 << 0)
        self.__write_reg(0, config)
        self.ce(1)
        utime.sleep_us(130)

    def sendMessage(self, msg):
        self.csn(0)
        self.spi.write(bytearray([0b11100001]))
        self.csn(1)

        status = self.__read_reg(7)[0]
        status |= (1 << 4)
        self.__write_reg(7, status)

        data = bytearray(msg)
        data.extend(bytearray(32 - len(msg)))

        reg = [0b10100000]
        self.csn(0)
        self.spi.write(bytearray(reg))

        self.spi.write(bytearray(data))

        self.csn(1)

        self.ce(1)

        utime.sleep_us(10)

        self.ce(0)
        status = self.__read_reg(7)[0]
        while (status & (1 << 5)) == 0 and (status & (1 << 4)) == 0:
            status = self.__read_reg(7)[0]
            # print()
            # print(bin(status))
            # print(bin(self.__read_reg()(0x17)[0]))
            # print(bin(self.__read_reg()(0x0)[0]))
            utime.sleep(1)


        status |= (1 << 4) | (1 << 5)
        self.__write_reg(7, status)

        self.modeRX()

    def newMessage(self):
        status = self.__read_reg(7)[0]  # 6
        fstatus = self.__read_reg(0x17)[0]  # 1

        result = (not (0b00000001 & fstatus)) or (0b01000000 & status)

        status |= (1 << 4) | (1 << 5)
        self.__write_reg(7, status)

        return result

    def readMessage(self):
        #self.modeRX()
        reg = [0b01100001]

        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(32)
        self.csn(1)
        status = self.__read_reg(7)[0]
        status |= (1 << 6)
        self.__write_reg(7, status)

        return result

# from machine import SPI, Pin
# nrf_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10), mosi=Pin(11), miso=Pin(8))  # noqa
# nrf = NRF()  # noqa

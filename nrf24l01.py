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

import utime
from micropython import const


class NRF24L01:
    """
    Class to handle nRF24L01 functionality
    """

    # nRF24L01 registers
    CONFIG = const(0x00)  # Configuration Register p. 53
    EN_AA = const(0x01)  # Enable 'Auto Acknowledgment'  p. 53
    EN_RXADDR = const(0x02)  # Enabled RX Addresses p. 53
    SETUP_AW = const(0x03)  # Setup Of Address Widths p. 54
    SETUP_RETR = const(0x04)  # Setup of Automatic Retransmission p. 54
    RF_CH = const(0x05)  # RF Channel p. 54
    RF_SETUP = const(0x06)  # RF Setup Register p. 54
    STATUS = const(0x07)  # Status Register p. 55
    OBSERVE_TX = const(0x08)  # Transmit Observe Register p. 55
    CD = const(0x09)  # Carrier Detect p. 55
    RX_ADDR_P0 = const(0x0a)  # Receive Address Data Pipe 0 p. 55
    RX_ADDR_P1 = const(0x0b)  # Receive Address Data Pipe 1 p. 55
    RX_ADDR_P2 = const(0x0c)  # Receive Address Data Pipe 2 p. 55
    RX_ADDR_P3 = const(0x0d)  # Receive Address Data Pipe 3 p. 55
    RX_ADDR_P4 = const(0x0e)  # Receive Address Data Pipe 4 p. 55
    RX_ADDR_P5 = const(0x0f)  # Receive Address Data Pipe 5 p. 55
    TX_ADDR = const(0x10)  # Transmit Address p. 56
    RX_PW_P0 = const(0x11)  # Number Of Bytes In RX Payload In Data Pipe 0 p. 56
    RX_PW_P1 = const(0x12)  # Number Of Bytes In RX Payload In Data Pipe 1 p. 56
    RX_PW_P2 = const(0x13)  # Number Of Bytes In RX Payload In Data Pipe 2 p. 56
    RX_PW_P3 = const(0x14)  # Number Of Bytes In RX Payload In Data Pipe 3 p. 56
    RX_PW_P4 = const(0x15)  # Number Of Bytes In RX Payload In Data Pipe 4 p. 56
    RX_PW_P5 = const(0x16)  # Number Of Bytes In RX Payload In Data Pipe 2 p. 57
    FIFO_STATUS = const(0x17)  # FIFO Status Register p. 57
    DYNPD = const(0x1c)  # Enable Dynamic Payload Length p. 58
    FEATURE = const(0x1d)  # Feature Register p. 58

    def __init__(self, spi, csn, ce):
        """
        Params:
            spi: object
            csn: object
            ce: object
        """
        self.csn = csn
        self.ce = ce
        self.spi = spi
        utime.sleep_ms(11)
        self.__init_nrf()

    def __init_nrf(self, channel=60, channel_name='gyroc', packet_size=32):
        """
        Private method to handle init of nrf

        Params:
            channel: int, optional
            channel_name: str, optional
            packet_size: int, optional
        """
        self.csn(1)
        self.ce(0)
        utime.sleep_ms(11)
        self.__write_cmd(0, 0b00001010)  # config
        utime.sleep_us(1500)
        self.__write_cmd(1, 0b00000011)  # no ack
        self.__write_cmd(5, channel)
        self.__write_cmd(0x0a, channel_name)
        self.__write_cmd(0x10, channel_name)
        self.__write_cmd(0x11, packet_size)

    def __read_cmd(self, reg, size=1):
        """
        Private method to read command to nrf

        Params:
            reg: int
            size: int, optional

        Returns:
            int
        """
        reg = [0b00011111 & reg]
        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(size)
        self.csn(1)
        return result

    def __write_cmd(self, reg, data):
        """
        Private method to write command to nrf

        Params:
            reg: int
            data: bytearray

        Returns:
            int
        """
        reg = [0b00100000 | (0b00011111 & reg)]
        self.csn(0)
        self.spi.write(bytearray(reg))
        data = [data] if type(data) == type(1) else data  # noqa
        self.spi.write(bytearray(data))
        self.csn(1)

    def __mode_tx(self):
        """
        Private method to handle enabling nrf transmit mode
        """
        reg = self.__read_cmd(0)[0]
        reg &= ~(1 << 0)
        self.__write_cmd(0, reg)
        self.ce(0)
        utime.sleep_us(130)

    def __mode_rx(self):
        """
        Private method to handle enabling nrf receive mode
        """
        reg = self.__read_cmd(0)[0]
        reg |= (1 << 0)
        self.__write_cmd(0, reg)
        self.ce(1)
        utime.sleep_us(130)

    def __new_text(self):
        """
        Private method to handle checking of a raw new text received

        Returns:
            int
        """
        regfs = self.__read_cmd(0x17)[0]
        regs = self.__read_cmd(7)[0]
        return (not (0b00000001 & regfs)) or (0b01000000 & regs)

    def __read_text(self, size=32):
        """
        Private method to handle reading of a raw new text received

        Params:
            size: int, optional

        Returns:
            bytearray
        """
        self.__mode_rx()
        reg = [0b01100001]
        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(size)
        self.csn(1)
        self.__write_cmd(0x07, 0b01000000)  # clear status flags
        return result

    def send(self, text, size=32):
        """
        Method to handle sending a new text

        Params:
            text: str
            size: int, optional
        """
        self.__mode_tx()
        reg = [0b10100000]
        self.csn(0)
        self.spi.write(bytearray([0b11100001]))
        self.csn(1)
        self.csn(0)
        self.spi.write(bytearray(reg))
        local_text = bytearray(text)
        local_text.extend(bytearray(size - len(local_text)))
        self.spi.write(bytearray(local_text))
        self.csn(1)
        self.ce(1)
        utime.sleep_us(10)
        for i in range(0, 10000):
            reg = self.__read_cmd(7)[0]
            if reg & 0b00110000:
                break
        self.ce(0)
        self.__write_cmd(7, 0b00110000)  # clear status flags

    def recv(self):
        """
        Method to handle receiving a new message
        """
        self.__mode_rx()
        if self.__new_text():  # print any incoming message
            print(''.join([chr(i) for i in self.__read_text()]))

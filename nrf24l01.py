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
from machine import SPI, Pin



class NRF:
    def __init__(self, port=1, sck=10, mosi=11, miso=8, csn=3, ce=0, speed=4000000):
        utime.sleep_ms(11)
        self.ce = Pin(ce, 1)
        self.csn = Pin(csn, 1)

        self.spi = SPI(port, speed, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))

        self.ce(0)
        self.csn(1)

    def readReg(self, reg, size=1):
        reg = [0b00011111 & reg]

        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(size)
        self.csn(1)

        return result

    def writeReg(self, reg, value):
        reg = [0b00100000 | (0b00011111 & reg)]

        value = [value] if type(value) == type(1) else value

        self.csn(0)
        self.spi.write(bytearray(reg))
        self.spi.write(bytearray(value))
        self.csn(1)

    def config(self):
        self.csn(1)
        self.ce(0)

        self.writeReg(0, 0b00001010)
        utime.sleep_ms(2)

        # print(bin(self.readReg(0)[0]))
        utime.sleep_ms(2000)

        self.writeReg(1, 0b00000011)
        self.writeReg(3, 0b00000011)

        self.writeReg(5, 60)

        self.writeReg(6, 0b00001111)

        self.writeReg(0x0a, "gyroc")
        self.writeReg(0x10, "gyroc")

        self.writeReg(0x11, 32)

    def modeTX(self):
        config = self.readReg(0)[0]
        config &= ~(1 << 0)
        self.writeReg(0, config)
        self.ce(0)
        utime.sleep_us(130)

    def modeRX(self):
        config = self.readReg(0)[0]
        config |= (1 << 0)
        self.writeReg(0, config)
        self.ce(1)
        utime.sleep_us(130)

    def sendMessage(self, msg):
        self.modeTX()

        self.csn(0)
        self.spi.write(bytearray([0b11100001]))
        self.csn(1)

        status = self.readReg(7)[0]
        status |= (1 << 4)
        self.writeReg(7, status)

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
        status = self.readReg(7)[0]
        while (status & (1 << 5)) == 0 and (status & (1 << 4)) == 0:
            status = self.readReg(7)[0]
            # print()
            # print(bin(status))
            # print(bin(self.readReg(0x17)[0]))
            # print(bin(self.readReg(0x0)[0]))
            utime.sleep(1)


        status |= (1 << 4) | (1 << 5)
        self.writeReg(7, status)

        self.modeRX()

    def newMessage(self):
        status = self.readReg(7)[0]  # 6
        fstatus = self.readReg(0x17)[0]  # 1

        result = (not (0b00000001 & fstatus)) or (0b01000000 & status)

        status |= (1 << 4) | (1 << 5)
        self.writeReg(7, status)

        return result

    def readMessage(self):
        reg = [0b01100001]

        self.csn(0)
        self.spi.write(bytearray(reg))
        result = self.spi.read(32)
        self.csn(1)
        status = self.readReg(7)[0]
        status |= (1 << 6)
        self.writeReg(7, status)

        return result

#sd_card_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10), mosi=Pin(11), miso=Pin(8))  # noqa
nrf = NRF()  # noqa
nrf.config()


def recv():
    nrf.modeRX()
    print(bin(nrf.readReg(0)[0]))
    led = Pin(25, 1)
    led.toggle()
    if nrf.newMessage() > 0:
        print("msg: ", "".join([chr(i) for i in nrf.readMessage()]))


def send():
    #nrf.modeTX()
    for _ in range(100):
        nrf.sendMessage("From 2: ")
        utime.sleep(0.001)

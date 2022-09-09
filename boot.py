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

from machine import Pin, SPI
import uos
import neopixel

from sd_card import SDCard

# init neo_pixel to ensure badge is running
np = neopixel.NeoPixel(Pin(5), 24)
np[11] = (0, 255, 0)
np[2] = (0, 255, 0)
np[5] = (0, 255, 0)
np[8] = (0, 255, 0)
np.write()

# sd card config
try:
    sd_card_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                    mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
    # init sd card
    sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
    # mount sd card filesystem
    vfs = uos.VfsFat(sd_card)
    uos.mount(vfs, '/sd')
    np[12] = (255, 0, 0)
    np.write()
except:  # noqa
    try:
        sd_card_spi = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                    mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
        # init sd card
        sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
        # mount sd card filesystem
        vfs = uos.VfsFat(sd_card)
        uos.mount(vfs, '/sd')
        np[13] = (255, 0, 0)
        np.write()
    except:  # noqa
        try:
            sd_card_spi = SPI(1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                        mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
            # init sd card
            sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
            # mount sd card filesystem
            vfs = uos.VfsFat(sd_card)
            uos.mount(vfs, '/sd')
            np[14] = (255, 0, 0)
            np.write()
        except:  # noqa
            try:
                sd_card_spi = SPI(1, baudrate=100000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                            mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
                # init sd card
                sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
                # mount sd card filesystem
                vfs = uos.VfsFat(sd_card)
                uos.mount(vfs, '/sd')
                np[15] = (255, 0, 0)
                np.write()
            except:  # noqa
                sd_card_spi = SPI(1, baudrate=50000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                            mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
                # init sd card
                sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
                # mount sd card filesystem
                vfs = uos.VfsFat(sd_card)
                uos.mount(vfs, '/sd')
                np[16] = (255, 0, 0)
                np.write()

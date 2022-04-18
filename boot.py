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

from machine import Pin, SPI
import uos

import sd_card
import nrf
import share_spi1

SD_CARD_CS = Pin(9, Pin.OUT)
NRF_CS = Pin(1, Pin.OUT)

# sd card config
sd_card_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10), mosi=Pin(11),
                  miso=Pin(8))

# init sd card
sd_card = sd_card.SDCard(sd_card_spi, SD_CARD_CS)

# mount sd card filesystem
vfs = uos.VfsFat(sd_card)
uos.mount(vfs, '/sd')

# nrf config
if usys.platform == 'rp2':  # Software SPI
    cfg = {'spi': 1, 'copi': 11, 'cipo': 8, 'sck': 10, 'csn': NRF_CS, 'ce': 2}
else:
    raise ValueError('Unsupported platform {}'.format(usys.platform))
PIPES = (b'\xe1\xf0\xf0\xf0\xf0', b'\xe1\xf0\xf0\xf0\xf0')

# init nrf
nrf = nrf.NRF()

# init share_spi1
share_spi1 = share_spi1.Device()  # ensure both sd card cs and nrf cs are set high as they are not in use
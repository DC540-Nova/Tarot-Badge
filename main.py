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

# pip install mpremote
# mpremote connect /dev/tty.u* cp main.py :
# mpremote connect /dev/tty.u* rm ids
# mpremote connect /dev/tty.u* cp main.py :/sd/
# mpremote connect /dev/tty.u* cp *.* :/sd/
# mpremote connect /dev/tty.u* ls
# mpremote connect /dev/tty.u* cat games_won
# mpremote connect /dev/tty.u* exec 'import main;main.img_test()'
# screen /dev/tty.u*

from machine import Pin, SPI
import uos

from sd_card import SDCard
from neo_pixel import NeoPixel
from nrf24l01 import NRF
from microcontroller import Microcontroller
from encryption import Encryption
from touch import Touch
from file_manager import FileManager
from demo import Demo
from tarot import Tarot
from bad_advice import BadAdvice
from game import Game
from morse_code import MorseCode
from pair import Pair
from menu import Menu
import data


def status(sd_card_status, button_status, display_status, neo_pixel_status, nrf_status):  # noqa
    """
    Function to check status of peripherals

    Params:
        sd_card_status: str
        button_status: str
        display_status: str
        neo_pixel_status: str
        nrf_status: str
    """
    title = 8
    line_3 = 56
    line_4 = 80
    line_5 = 104
    line_6 = 128
    line_7 = 152
    print(sd_card_status)
    display.text('status', y=title, color=0b11001111011011111010001, wrap=False, clear=True, timed=False, off=True)
    display.text(sd_card_status, y=line_3, wrap=False, clear=False, timed=False, off=True)
    print(button_status)
    display.text(button_status, y=line_4, wrap=False, clear=False, timed=False, off=True)
    print(display_status)
    display.text(display_status, y=line_5, wrap=False, clear=False, timed=False, off=True)
    print(neo_pixel_status)
    display.text(neo_pixel_status, y=line_6, wrap=False, clear=False, timed=False, off=True)
    print(nrf_status)
    display.text(nrf_status, y=line_7, wrap=False, clear=False, off=False)


# init neo_pixel to ensure badge is running
try:
    import neopixel
    np = neopixel.NeoPixel(Pin(5), 24)
    np[11] = (0, 255, 0)
    np[2] = (0, 255, 0)
    np[5] = (0, 255, 0)
    np[8] = (0, 255, 0)
    np.write()
except:  # noqa
    pass

# set global fail state to False and if an exception is hit trigger fail to halt badge from running
fail = False

# sd card config
sd_card = None
sd_card_status = None
try:
    sd_card_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                      mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
    sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
    vfs = uos.VfsFat(sd_card)
    uos.mount(vfs, '/sd')
    sd_card_status = 'sd_card: PASS (4M)'
except Exception as e:  # noqa
    try:
        sd_card_spi = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                          mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
        sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
        vfs = uos.VfsFat(sd_card)
        uos.mount(vfs, '/sd')
        sd_card_status = 'sd_card: PASS (1M)'
    except:  # noqa
        try:
            sd_card_spi = SPI(1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                              mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
            sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
            vfs = uos.VfsFat(sd_card)
            uos.mount(vfs, '/sd')
            sd_card_status = 'sd_card: PASS (500k)'
        except:  # noqa
            try:
                sd_card_spi = SPI(1, baudrate=100000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
                                  sck=Pin(10, Pin.OUT), mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
                sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
                vfs = uos.VfsFat(sd_card)
                uos.mount(vfs, '/sd')
                sd_card_status = 'sd_card: PASS (100k)'
            except:  # noqa
                sd_card_spi = SPI(1, baudrate=50000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
                                  sck=Pin(10, Pin.OUT), mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
                sd_card = SDCard(sd_card_spi, cs=Pin(9, Pin.OUT))
                vfs = uos.VfsFat(sd_card)
                uos.mount(vfs, '/sd')
                sd_card_status = 'sd_card: PASS (50k)'

# button config
button_left = 21
button_right = 22
button_up = 19
button_down = 18
button_submit = 17
button_extra = 16
button_status = None

# display config
display = None
display_status = None
try:
    display_spi = SPI(0, baudrate=40000000, sck=Pin(6, Pin.OUT), mosi=Pin(7, Pin.OUT))
    from ili9341 import Display
    display = Display(display_spi, dc=Pin(15, Pin.OUT), cs=Pin(13, Pin.OUT), rst=Pin(14, Pin.OUT))
    display_status = 'display: PASS'
except:  # noqa
    display_status = 'display: FAIL'
    fail = True

# neo_pixel config
neo_pixel = None
neo_pixel_status = None
try:
    LED_PIN = 5
    LED_COUNT = 24
    neo_pixel = NeoPixel(Pin, LED_PIN, LED_COUNT)
    neo_pixel_status = 'neo_pixel: PASS'
except:  # noqa
    neo_pixel_status = 'neo_pixel: FAIL'
    fail = True

# nrf config
nrf = None
nrf_status = None
try:
    nrf_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                  mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
    nrf = NRF(nrf_spi, csn=Pin(3, Pin.OUT), ce=Pin(0, Pin.OUT))
    nrf_status = 'nrf: PASS'
except:  # noqa
    nrf_status = 'nrf: FAIL'
    fail = True

# microcontroller config
microcontroller = Microcontroller()

# encryption config
encryption = Encryption()

# touch config
try:
    touch = Touch(button_up, button_down, button_left, button_right, button_submit, button_extra, display)  # noqa
    button_status = 'button: PASS'
except:  # noqa
    button_status = 'button: FAIL'
    fail = True

# file_manager config
file_manager = FileManager(touch, display, neo_pixel)  # noqa

# demo config
demo = Demo(file_manager, touch, display, neo_pixel, data)

# tarot config
tarot = Tarot(file_manager, touch, display, nrf, neo_pixel, data.cards)

# bad_advice config
bad_advice = BadAdvice(touch, display, neo_pixel)

# morse_code config
morse_code = MorseCode(encryption, neo_pixel, neo_pixel.RED)

# game config
game = Game(file_manager, touch, display, tarot, morse_code, encryption)

# pair config
pair = Pair(microcontroller, file_manager, display, neo_pixel, game, morse_code, nrf, data)

# menu config
menu = Menu(file_manager, touch, display, neo_pixel, game, tarot, bad_advice, pair, demo, data)

if __name__ == '__main__':
    status(sd_card_status, button_status, display_status, neo_pixel_status, nrf_status)
    if not fail:
        while True:
            try:
                try:
                    display.image('sd/dc540_logo.raw')
                    demo.play()
                    menu.system()
                # except Exception as e:  # noqa
                #     print(e)
                except:  # noqa
                    pass
            except:  # noqa
                while True:
                    pass

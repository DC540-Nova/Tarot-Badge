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
# mpremote connect /dev/tty.u* rm ili9341.py
# mpremote connect /dev/tty.u* cp main.py :/sd/
# mpremote connect /dev/tty.u* cp *.* :/sd/
# mpremote connect /dev/tty.u* ls
# mpremote connect /dev/tty.u* cat games_won
# mpremote connect /dev/tty.u* exec 'import main;main.img_test()'
# screen /dev/tty.u*

from config import BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display, neo_pixel, \
    nrf
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

microcontroller = Microcontroller()
encryption = Encryption()
touch = Touch(BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display)
file_manager = FileManager(touch, display, neo_pixel)
demo = Demo(touch, display, neo_pixel)
tarot = Tarot(touch, display, data.cards)
bad_advice = BadAdvice(touch, display, data.bad_advice)
morse_code = MorseCode(encryption, neo_pixel, neo_pixel.RED)
game = Game(touch, file_manager, display, tarot, morse_code, encryption)
pair = Pair(microcontroller, file_manager, display, neo_pixel, morse_code, nrf, data)
menu = Menu(touch, display, neo_pixel, game, tarot, bad_advice, data)

if __name__ == '__main__':
    # while True:
    #     try:
    #         try:
    #             # demo.play()
    #             file_manager.update_games_won()
    #             menu.system()
    #         except KeyboardInterrupt:
    #             pass
    #     except KeyboardInterrupt:
    #         pass
    pass


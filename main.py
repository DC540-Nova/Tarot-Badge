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
    nrf, deck
from microcontroller import Microcontroller
from button import Button
from encryption import Encryption
from file_manager import FileManager
from demo import Demo
from game import Game
from tarot import Tarot
from morse_code import MorseCode
from pair import Pair
from menu import Menu
import data

microcontroller = Microcontroller()
button = Button(BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display)
encryption = Encryption()
file_manager = FileManager(button, display, neo_pixel)
demo = Demo(display, neo_pixel)
game = Game(button, file_manager, display)
tarot = Tarot(button, display, data.cards)
morse_code = MorseCode(encryption, neo_pixel, neo_pixel.RED)
pair = Pair(microcontroller, file_manager, display, neo_pixel, morse_code, nrf, data)
menu = Menu(button, display, neo_pixel, game, tarot, data, deck)


if __name__ == '__main__':
    demo.play()
    file_manager.update_games_won()
    menu.system()

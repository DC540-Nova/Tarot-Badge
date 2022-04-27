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
# mpremote cp main.py :
# mpremote exec 'import main'
# mpremote connect /dev/tty.u* cp main.py :
# mpremote connect /dev/tty.u* rm ili9341.py :
# mpremote connect /dev/tty.u* cp main.py :/sd/
# mpremote connect /dev/tty.u* cp *.* :/sd/
# mpremote connect /dev/tty.u* exec 'import main;main.img_test()'
# screen /dev/tty.u*
# ~/Documents/pico/micropython/mpy-cross/mpy-cross ili9341.py

import _thread
import random
import gc

from config import *


def bg_task():
    """
    Function to test demo multi-threadded functionality
    """
    gc.collect()
    hex1 = [32, 31, 30, 27, 28, 29, 32]
    paths = [28, 30, 29, 26, 22, 21, 23, 24, 19, 14, 13, 16, 17, 12, 11, 10, 8, 6, 3, 5, 2, 1]
    for count in range(20):
        for my_LED in hex1:
            neo_pixel.led_on(paths[my_LED - 11], COLORS[random.randint(1, 7)])
            if count == 19:
                neo_pixel.led_clear()
                _thread.exit()  # noqa


def sd_test():
    """
    Function to test sd card functionality
    """
    with open('test01.txt', 'w') as f:
        f.write('Hello, Baab!\r\n')
        f.write('This is the United States calling are we reaching?\r\n')
    with open('test01.txt', 'r') as f:
        data = f.read()
        print(data)


def img_test():
    """
    Function to test img display functionality
    """
    display.handle_threading_setup()
    _thread.start_new_thread(bg_task, ())  # noqa
    display.image('sd/00-TheFool.raw', multithreading=True)
    display.handle_threading_teardown()
    display.handle_threading_setup()
    _thread.start_new_thread(bg_task, ())  # noqa
    display.image('sd/01-TheMagician.raw', multithreading=True)
    display.handle_threading_teardown()
    display.handle_threading_setup()
    _thread.start_new_thread(bg_task, ())  # noqa
    display.image('sd/02-TheHighPriestess.raw', multithreading=True)
    display.handle_threading_teardown()


def questions():
    """
    Function to test questions on display
    """
    display.text('This is a long message I do hope it will wrap i will cry badly if it does not and blame babba.')


sd_test()
img_test()
questions()

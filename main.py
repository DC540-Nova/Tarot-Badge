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
# mpremote connect /dev/tty.u* exec 'import main'
# mpremote connect /dev/tty.u* cp main.py :/sd/
# mpremote connect /dev/tty.u* cp *.* :/sd/

import utime
import _thread
import random
import gc

from ili9341 import color565
import neo_pixel
import demo

from config import *

neo_pixel = neo_pixel.NeoPixel(Pin)

hex1 = [32, 31, 30, 27, 28, 29, 32]
paths = [28, 30, 29, 26, 22, 21, 23, 24, 19, 14, 13, 16, 17, 12, 11, 10, 8, 6, 3, 5, 2, 1]


def bg_task():
    """
    Function to test demo multi-threadded functionality
    """
    gc.collect()
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
    display.clear()
    _thread.start_new_thread(bg_task, ())  # noqa
    display.draw_image('sd/00-TheFool.raw', draw_speed=1024)
    display_on.value(1)
    utime.sleep(1)
    display_on.value(0)
    _thread.start_new_thread(bg_task, ())  # noqa
    display.draw_image('sd/01-TheMagician.raw', draw_speed=1024)
    display_on.value(1)
    utime.sleep(1)
    display_on.value(0)
    _thread.start_new_thread(bg_task, ())  # noqa
    display.draw_image('sd/02-TheHighPriestess.raw', draw_speed=1024)
    display_on.value(1)
    utime.sleep(1)
    display_on.value(0)


def main_menu():
    """
    Function to display the main menu
    """
    display.clear()
    display.draw_text(0, 0, 'MAIN MENU', color565(255, 128, 0), unispace)
    display.draw_text(0, 25, 'up: Badge ID', color565(255, 255, 0), unispace)
    display.draw_text(0, 50, 'down: Games', color565(255, 255, 0), unispace)
    display.draw_text(0, 75, 'lt: Phonebooth', color565(255, 255, 0), unispace)
    display_on.value(1)
    utime.sleep(1)
    display_on.value(0)


def questions():
    """
    Function to test questions on display
    """
    display.clear()
    display.draw_text(0, 0, 'This is a long message I do hope it will wrap i will cry badly '
                            'if it does not and blame babba.', color565(255, 128, 0), unispace)
    display_on.value(1)
    utime.sleep(5)
    display_on.value(0)


def test_sao_comms():
    from machine import UART
    uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

    txData = b'hello world\n\r'
    uart0.write(txData)
    time.sleep(0.1)
    rxData = bytes()
    while uart0.any() > 0:
        rxData += uart0.read(1)

    print(rxData.decode('utf-8'))


# sd_test()
# img_test()
# main_menu()
# questions()
# demo.play()
test_sao_comms()

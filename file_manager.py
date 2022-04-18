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

import os
from utime import sleep

from config import *


def write_ids_file(str_ids):
    """
    Function to write the ids of the badges collected

    Params:
        str_ids: str
    """
    try:
        with open('ids', 'w') as file:
            file.write(str_ids)
    except OSError:
        pass


def read_ids_file():
    """
    Function to read the id's paired

    Returns:
        str
    """
    try:
        with open('ids', 'r') as file:
            str_ids = file.read()
            return str_ids
    except OSError:
        pass


def write_status_file(str_status):
    """
    Function to write the game status

    Params:
        str_status: str
    """
    try:
        with open('status', 'w') as file:
            file.write(str_status)
    except OSError:
        pass


def read_status_file():
    """
    Function to read the overall status achieved

    Returns:
        str
    """
    try:
        with open('status', 'r') as file:
            str_status = file.read()
            return str_status
    except OSError:
        pass


def update_status(got_correct_answer=False):
    """
    Function to update the status and set the LED's

    Params:
        got_correct_answer: bool, optional
    """
    # Avoid circular import issue
    from neo_pixel import NeoPixel
    neo_pixel = NeoPixel(Pin)
    try:
        with open('status', 'r') as file:
            str_status = file.read()
            str_status = list(str_status.split(' '))
            str_status = str_status[0:-1]
            status = [int(element) for element in str_status]
            spheres = [0, 4, 9, 7, 15, 18, 20, 25, 27, 31]
            if got_correct_answer:
                most_recent_game_won = status[-1]
                # Account for zero-index
                most_recent_game_won -= 1
                neo_pixel.breathing_led_on(spheres[most_recent_game_won])
                # Display the remaining games without animation
                for game in status:
                    game_offset = game - 1
                    neo_pixel.led_on(spheres[game_offset], RED)
            else:
                for game in status:
                    game_offset = game - 1
                    neo_pixel.led_on(spheres[game_offset], RED)
    except OSError:
        pass


def clear_ids_file():
    """
    Function to clear status file after winning a game
    """
    try:
        os.remove('ids')
        with open('ids', 'w') as file:
            file.write('')
    except OSError:
        pass


def clear_status_file():
    """
    Function to clear status file after winning a game
    """
    try:
        os.remove('status')
        with open('status', 'w') as file:
            file.write('')
    except OSError:
        pass


def check_files():
    """
    Function to check status file if exists

    Returns:
        bool
    """
    try:
        with open('status', 'r') as file:  # noqa
            pass
    except OSError:
        with open('status', 'w') as file:
            file.write('')
    try:
        with open('ids', 'r') as file:  # noqa
            pass
    except OSError:
        with open('ids', 'w') as file:
            file.write('')


def reset(file, sleep_time=2):
    """
    Method to reset a file

    Params:
        file: str
        sleep_time: int, optional
    """
    # Avoid circular import issue
    from button_input import ButtonInput
    from neo_pixel import NeoPixel
    button_input = ButtonInput()
    neo_pixel = NeoPixel(Pin)
    if file == 'status':
        message = 'ARE YOU SURE YOU WANT TO RESET GAME?'
    elif file == 'ids':
        message = 'ARE YOU SURE YOU WANT TO RESET PAIRS?'
    display.scroll_text([[0,0,message]], len(message))  # noqa
    sleep(sleep_time)
    reset = button_input.get_response(input_type='y_n_letters')  # noqa
    if reset == 'Y':
        if file == 'status':
            message = 'RESETTING GAME!'
        elif file == 'ids':
            message = 'RESETTING STATUS!'
        display.scroll_text([[0, 0, message]], len(message))
        sleep(sleep_time)
        if file == 'ids':
            clear_ids_file()
        if file == 'status':
            clear_status_file()
    else:
        pass
    neo_pixel.led_clear()
    display.clear()
    update_status()

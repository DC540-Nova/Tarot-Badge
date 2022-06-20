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

from config import display, neo_pixel
import button


def write_ids_file(ids):
    """
    Function to write to the ids file

    Params:
    ids: str
    """
    try:
        with open('ids', 'w') as f:
            f.write(ids)
    except OSError:
        pass


def read_ids_file():
    """
    Function to read the ids file

    Returns:
        str
    """
    try:
        with open('ids', 'r') as f:
            ids = f.read()
            return ids
    except OSError:
        pass


def write_games_won_file(games_won):
    """
    Function to write to the games_won file

    Params:
        str_status: str
    """
    try:
        with open('games_won', 'w') as f:
            f.write(games_won)
    except OSError:
        pass


def read_games_won_file():
    """
    Function to read the games_won file

    Returns:
        str
    """
    try:
        with open('games_won', 'r') as f:
            games_won = f.read()
            return games_won
    except OSError:
        pass


def update_games_won():
    """
    Function to update the games won by getting the games_won from file and setting the relevant neopixels
    """
    try:
        with open('games_won', 'r') as f:
            games_won = f.read()
            games_won = list(games_won.split(' '))
            if '01' in games_won:
                neo_pixel.on(0)
            if '02' in games_won:
                neo_pixel.on(1)
            if '03' in games_won:
                neo_pixel.on(3)
            if '04' in games_won:
                neo_pixel.on(4)
            if '05' in games_won:
                neo_pixel.on(5)
    except OSError:
        pass


def clear_ids_file():
    """
    Function to clear the ids file by resetting it
    """
    try:
        os.remove('ids')
        with open('ids', 'w') as f:
            f.write('')
    except OSError:
        pass


def clear_games_won_file():
    """
    Function to clear games_won file by resetting it
    """
    try:
        os.remove('games_won')
        with open('games_won', 'w') as f:
            f.write('')
    except OSError:
        pass


def check_files():
    """
    Function to check status file if exists

    Returns:
        bool
    """
    try:
        with open('games_won', 'r') as f:  # noqa
            pass
    except OSError:
        with open('games_won', 'w') as f:
            f.write('')
    try:
        with open('ids', 'r') as f:  # noqa
            pass
    except OSError:
        with open('ids', 'w') as f:
            f.write('')


def reset(file, sleep_time=2):
    """
    Method to reset a file

    Params:
        file: str
        sleep_time: int, optional
    """
    if file == 'games_won':
        message = 'ARE YOU SURE YOU WANT TO RESET GAME?'
    elif file == 'ids':
        message = 'ARE YOU SURE YOU WANT TO RESET PAIRS?'
    display.scroll_text([[0,0,message]], len(message))  # noqa
    sleep(sleep_time)
    reset = button.yes_no()  # noqa
    if reset == 'yes':
        if file == 'games_won':
            message = 'RESETTING GAME!'
        elif file == 'ids':
            message = 'RESETTING STATUS!'
        display.scroll_text([[0, 0, message]], len(message))
        sleep(sleep_time)
        if file == 'ids':
            clear_ids_file()
        if file == 'games_won':
            clear_games_won_file()
    neo_pixel.clear()
    display.clear()
    update_games_won()

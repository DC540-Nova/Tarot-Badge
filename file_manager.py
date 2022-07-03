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


class FileManager:
    """
    Base class to handle a file manager object and functionality for persistence
    """

    def __init__(self, display, neo_pixel, button):
        """
        Params:
            display: object
            neo_pixel: object
            button: object
        """
        self.display = display
        self.neo_pixel = neo_pixel
        self.button = button

    @staticmethod
    def write_ids_file(ids):
        """
        Static method to write to the ids file

        Params:
        ids: str
        """
        try:
            with open('ids', 'w') as f:
                f.write(ids)
        except OSError:
            pass

    @staticmethod
    def read_ids_file():
        """
        Static method to read the ids file

        Returns:
            str
        """
        try:
            with open('ids', 'r') as f:
                ids = f.read()
                return ids
        except OSError:
            with open('ids', 'w') as f:
                f.write('')
            with open('ids', 'r') as f:
                ids = f.read()
                return ids

    @staticmethod
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

    @staticmethod
    def read_games_won_file():
        """
        Static method to read the games_won file

        Returns:
            str
        """
        try:
            with open('games_won', 'r') as f:
                games_won = f.read()
                return games_won
        except OSError:
            with open('games_won', 'w') as f:
                f.write('')
            with open('games_won', 'r') as f:
                games_won = f.read()
                return games_won

    @staticmethod
    def clear_ids_file():
        """
        Static method to clear the ids file by resetting it
        """
        try:
            os.remove('ids')
            with open('ids', 'w') as f:
                f.write('')
        except OSError:
            pass

    @staticmethod
    def clear_games_won_file():
        """
        Static method to clear games_won file by resetting it
        """
        try:
            os.remove('games_won')
            with open('games_won', 'w') as f:
                f.write('')
        except OSError:
            pass

    def update_games_won(self):
        """
        Method to update the games won by getting the games_won from file and setting the relevant neopixels
        """
        try:
            with open('games_won', 'r') as f:
                games_won = f.read()
                games_won = list(games_won.split(' '))
                print(games_won)
                print(type(games_won))
                if '1' in games_won:
                    self.neo_pixel.on(0)
                if '2' in games_won:
                    self.neo_pixel.on(1)
        except OSError:
            with open('games_won', 'w') as f:
                f.write('')
            with open('games_won', 'r') as f:
                games_won = f.read()
                games_won = list(games_won.split(' '))
                if '1' in games_won:
                    self.neo_pixel.on(0)
                if '2' in games_won:
                    self.neo_pixel.on(1)

    def reset(self, file, sleep_time=2):
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
        self.display.scroll_text([[0, 0, message]], len(message))  # noqa
        sleep(sleep_time)
        reset = self.button.yes_no()
        if reset == 'yes':
            if file == 'games_won':
                message = 'RESETTING GAME!'
            elif file == 'ids':
                message = 'RESETTING STATUS!'
            self.display.scroll_text([[0, 0, message]], len(message))
            sleep(sleep_time)
            if file == 'ids':
                self.clear_ids_file()
            if file == 'games_won':
                self.clear_games_won_file()
        self.update_games_won()

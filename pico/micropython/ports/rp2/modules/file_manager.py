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

import uos
from utime import sleep

from neopixel import NeoPixel


class FileManager:
    """
    Base class to handle a file manager object and functionality for persistence
    """

    def __init__(self, touch, display, neo_pixel):
        """
        Params:
            touch: object
            display: object
            neo_pixel: object
        """
        self.touch = touch
        self.display = display
        self.neo_pixel = neo_pixel
        self.games_won = None

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
        Static method to write to the games_won file

        Params:
            games_won: str
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
    def write_tarot_deck_folder(tarot_deck_folder):
        """
        Static method to write to the tarot deck folder file

        Params:
            tarot_deck_folder: str
        """
        try:
            with open('tarot_deck_folder', 'w') as f:
                f.write(tarot_deck_folder)
        except OSError:
            with open('tarot_deck_folder', 'w') as f:
                f.write('Rider-Waite')

    @staticmethod
    def read_tarot_deck_folder():
        """
        Static method to read to the tarot deck folder file

        Returns:
            str
        """
        try:
            with open('tarot_deck_folder', 'r') as f:
                tarot_deck_folder = f.read()
                return tarot_deck_folder
        except OSError:
            with open('tarot_deck_folder', 'w') as f:
                f.write('Rider-Waite')
            with open('tarot_deck_folder', 'r') as f:
                tarot_deck_folder = f.read()
                return tarot_deck_folder

    @staticmethod
    def clear_ids_file():
        """
        Static method to clear the ids file by resetting it
        """
        try:
            uos.remove('ids')
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
            uos.remove('games_won')
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
                won = 0
                self.games_won = f.read()
                self.games_won = list(self.games_won.split(' '))
                if '66' in self.games_won:
                    self.neo_pixel.on(0)
                    won += 1
                if '23' in self.games_won:
                    self.neo_pixel.on(1)
                    won += 1
                if '89' in self.games_won:
                    self.neo_pixel.on(2)
                    won += 1
                if '40' in self.games_won:
                    self.neo_pixel.on(3)
                    won += 1
                if '98' in self.games_won:
                    self.neo_pixel.on(4)
                    won += 1
                if '11' in self.games_won:
                    self.neo_pixel.on(5)
                    won += 1
                if '15' in self.games_won:
                    self.neo_pixel.on(6)
                    won += 1
                if '37' in self.games_won:
                    self.neo_pixel.on(7)
                    won += 1
                if '71' in self.games_won:
                    self.neo_pixel.on(8)
                    won += 1
                if '53' in self.games_won:
                    self.neo_pixel.on(9)
                    won += 1
                if '94' in self.games_won:
                    self.neo_pixel.on(10)
                    won += 1
                if '69' in self.games_won:
                    self.neo_pixel.on(11)
                    won += 1
                if won == 12:
                    self.neo_pixel.won()
        except OSError:
            with open('games_won', 'w') as f:
                f.write('')

    def reset(self, file):
        """
        Method to reset a file

        Params:
            file: str
            sleep_time: int, optional
        """
        message = ''
        if file == 'ids':
            message = 'ARE YOU SURE YOU WANT TO RESET PAIRS?'
        elif file == 'games_won':
            message = 'ARE YOU SURE YOU WANT TO RESET GAME? [A: Yes & B: No]'
        self.display.text(message, timed=False)
        reset = self.touch.yes_no()
        if reset == 'yes':
            if file == 'games_won':
                self.neo_pixel.clear(hard_clear=True)
                message = 'RESETTING GAME!'
            elif file == 'ids':
                message = 'RESETTING STATUS!'
            self.display.text(message)
            if file == 'ids':
                self.clear_ids_file()
            if file == 'games_won':
                self.clear_games_won_file()
        self.update_games_won()

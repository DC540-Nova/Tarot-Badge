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

import uos
from utime import sleep


class Menu:
    """
    Base class to handle a menu system
    """

    def __init__(self, touch, display, neo_pixel, game, tarot, data, deck='Rider-Waite'):
        """
        Params:
            touch: object
            display: object
            neo_pixel: object
            game: object
            tarot: object
            data: object
            deck: None
        """
        self.touch = touch
        self.display = display
        self.neo_pixel = neo_pixel
        self.game = game
        self.tarot = tarot
        self.data = data
        self.deck = deck
        self.text = None
        self.title = 8
        self.line_2 = 32
        self.line_3 = 56
        self.line_4 = 80
        self.line_5 = 104
        self.line_6 = 128
        self.line_7 = 152
        self.line_8 = 176
        self.line_9 = 200
        self.line_10 = 224

    def __populate(self, title, line_3='', line_4='', line_5='', line_6='', line_7='', line_8='', line_9='', line_10='',
                   title_color=0b11001111011011111010001):
        """
        Private method to populate a menu

        Params:
            title: str
            line_3: str, optional
            line_4: str, optional
            line_5: str, optional
            line_6: str, optional
            line_7: str, optional
            line_8: str, optional
            line_9: str, optional
            line_10: str, optional
            title_color: int, optional
        """
        self.text = title
        self.display.text(self.text, y=self.title, color=title_color, wrap=False, clear=True, timed=False, off=True)
        self.text = line_3
        self.display.text(self.text, y=self.line_3, wrap=False, clear=False, timed=False, off=True)
        self.text = line_4
        self.display.text(self.text, y=self.line_4, wrap=False, clear=False, timed=False, off=True)
        self.text = line_5
        self.display.text(self.text, y=self.line_5, wrap=False, clear=False, timed=False, off=True)
        self.text = line_6
        self.display.text(self.text, y=self.line_6, wrap=False, clear=False, timed=False, off=True)
        self.text = line_7
        self.display.text(self.text, y=self.line_7, wrap=False, clear=False, timed=False, off=True)
        self.text = line_8
        self.display.text(self.text, y=self.line_8, wrap=False, clear=False, timed=False, off=True)
        self.text = line_9
        self.display.text(self.text, y=self.line_8, wrap=False, clear=False, timed=False, off=True)
        self.text = line_10
        self.display.text(self.text, y=self.line_8, wrap=False, clear=False, timed=False, off=False)

    def __game_menu_1(self):
        """
        Private method to handle the game menu
        """
        self.__populate('game menu 1', 'l: tarot trivia', 'r: stego', 'u: re-enactment',
                        'd: scavenger hunt', 's: flash cards', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.__game_menu_tarot_trivia()
            elif self.touch.press(self.touch.button_right, 2):
                self.__game_menu_stego()
            elif self.touch.press(self.touch.button_up, 3):
                self.__game_menu_reenactment()
            elif self.touch.press(self.touch.button_down, 4):
                self.__game_menu_scavenger_hunt()
            elif self.touch.press(self.touch.button_submit, 5):
                self.__game_menu_flash_cards()
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_tarot_trivia(self):
        """
        Private method to handle the tarot trivia game
        """
        self.__populate('tarot trivia menu', 'l: instructions', 'r: play', 'u: practice', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.tarot_trivia_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                won_game = self.game.multiple_choice(self.data.tarot_trivia_game, '2', '1', 1, False)
                if won_game:
                    self.game.won(won_game)
            elif self.touch.press(self.touch.button_up, 3):
                self.game.multiple_choice_practice(self.data.tarot_trivia_game)
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_stego(self):
        """
        Private method to handle the stego game
        """
        self.__populate('stego menu', 'l: instructions', 'r: play', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.stego_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                # TODO: work this out with Betsy
                pass
            elif self.touch.press(self.touch.button_up, 3):
                pass
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_reenactment(self):
        """
        Private method to handle the reenactment game
        """
        self.__populate('reenactment menu', 'l: instructions', 'r: play', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.reenactment_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                # TODO: work this out with Betsy
                pass
            elif self.touch.press(self.touch.button_up, 3):
                pass
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_scavenger_hunt(self):
        """
        Private method to handle the scavenger hunt game
        """
        self.__populate('scavenger hunt menu', 'l: instructions', 'r: play', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.scavenger_hunt_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                # TODO: work this out with Betsy
                pass
            elif self.touch.press(self.touch.button_up, 3):
                pass
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_flash_cards(self):
        """
        Private method to handle the flash cards game
        """
        self.__populate('flash cards menu', 'l: instructions', 'r: play', 'u: practice', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.flash_cards_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                won_game = self.game.multiple_choice(self.data.flash_cards_game, '2', '1', 1, False)
                if won_game:
                    self.game.won(won_game)
            elif self.touch.press(self.touch.button_up, 3):
                self.game.practice(self.data.flash_cards_game)
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_2(self):
        """
        Private method to handle the game menu 2
        """
        self.__populate('game menu 2', 'l: fun deck', 'r: morse code', 'u: decryption', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.__game_menu_fun_deck()
            elif self.touch.press(self.touch.button_right, 2):
                self.__game_menu_morse_code()
            elif self.touch.press(self.touch.button_up, 3):
                pass
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_fun_deck(self):
        """
        Private method to handle the fun deck game
        """
        self.__populate('fun deck menu', 'l: instructions', 'r: play', 'u: practice', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.fun_deck_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                won_game = self.game.multiple_choice(self.data.fun_deck_game, '2', '1', 1, False)
                if won_game:
                    self.game.won(won_game)
            elif self.touch.press(self.touch.button_up, 3):
                self.game.multiple_choice_practice(self.data.fun_deck_game)
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __game_menu_morse_code(self):
        """
        Private method to handle the morse code game
        """
        self.__populate('morse code menu', 'l: instructions', 'r: play', 'u: practice-easy', 'd: practice-medium',
                        's: practice-advanced', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.morse_code_game_instructions)
            elif self.touch.press(self.touch.button_right, 2):
                won_game = self.game.multiple_choice(self.data.morse_code_game, '2', '1', 1, False)
                if won_game:
                    self.game.won(won_game)
            elif self.touch.press(self.touch.button_up, 3):
                pass
                #self.game.(self.data.morse_code_game_practice_easy)
            elif self.touch.press(self.touch.button_down, 4):
                pass
                #self.game.(self.data.morse_code_game_practice_medium)
            elif self.touch.press(self.touch.button_submit, 5):
                pass
                #self.game.(self.data.morse_code_game_practice_advanced)
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __tarot_reading_menu(self):
        """
        Private method to handle the tarot reading menu
        """
        self.__populate('tarot reading menu', 'l: choose deck', 'r: tarot reading', 'u: tarot scroll', 'e: main menu')
        deck_selected = False
        while True:
            if self.touch.press(self.touch.button_left, 1):
                try:
                    uos.chdir('sd')
                    folders = uos.listdir()
                    for folder in folders:
                        if folder == 'System Volume Information' or folder == '.fseventsd' or \
                                folder == '.Spotlight-V100' or folder == '.Trashes':
                            pass
                        else:
                            self.display.text(folder, timed=False)
                            while True:
                                if self.touch.press(self.touch.button_left, 1):
                                    self.deck = folder
                                    self.display.text('DECK CHANGED')
                                    deck_selected = True
                                    break
                                elif self.touch.press(self.touch.button_right, 2):
                                    break
                        if deck_selected:
                            break
                except OSError:
                    self.display.text('sd card is damaged')
            elif self.touch.press(self.touch.button_right, 2):
                self.tarot.reading(self.deck)
                self.__main_menu()
            elif self.touch.press(self.touch.button_up, 3):
                self.tarot.scroll(self.deck)
                self.__main_menu()
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6) or deck_selected:
                self.__main_menu()

    def __bad_advice_menu(self):
        """
        Private method to handle the bad advice menu
        """
        self.__populate('bad advice menu', '', '', '', '', '', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                pass
            elif self.touch.press(self.touch.button_right, 2):
                pass
            elif self.touch.press(self.touch.button_up, 3):
                pass
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __extras_menu(self):
        """
        Private method to handle the extras menu
        """
        self.__populate('extras menu', '', '', '', '', '', 'e: main menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                pass
            elif self.touch.press(self.touch.button_right, 2):
                pass
            elif self.touch.press(self.touch.button_up, 3):
                pass
            elif self.touch.press(self.touch.button_down, 4):
                pass
            elif self.touch.press(self.touch.button_submit, 5):
                pass
            elif self.touch.press(self.touch.button_extra, 6):
                self.__main_menu()

    def __main_menu(self):
        """
        Private method to handle the main menu
        """
        self.__populate('main menu', 'l: instructions', 'r: games 1 menu', 'u: games 2 menu', 'd: tarot menu',
                        's: bad advice menu', 'e: extras menu')
        while True:
            if self.touch.press(self.touch.button_left, 1):
                self.display.text(self.data.badge_instructions_1)
                self.display.text(self.data.badge_instructions_2)
                self.display.text(self.data.badge_instructions_3)
                break
            elif self.touch.press(self.touch.button_right, 2):
                self.__game_menu_1()
            elif self.touch.press(self.touch.button_up, 3):
                self.__game_menu_2()
            elif self.touch.press(self.touch.button_down, 4):
                self.__tarot_reading_menu()
            elif self.touch.press(self.touch.button_submit, 5):
                self.__bad_advice_menu()
            elif self.touch.press(self.touch.button_extra, 6):
                self.__extras_menu()

    def system(self):
        """
        Method to handle the menu system
        """
        # self.display.image('dc540_logo.raw')
        while True:
            self.__main_menu()

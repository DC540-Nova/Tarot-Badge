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


class Menu:
    """
    Base class to handle a menu system
    """

    def __init__(self, file_manager, touch, display, neo_pixel, game, tarot, bad_advice, pair, demo, data,
                 deck='Rider-Waite'):
        """
        Params:
            file_manager: object
            touch: object
            display: object
            neo_pixel: object
            game: object
            tarot: object
            bad_advice: object
            pair: object
            demo: object
            data: object
            deck: str, optional
        """
        self.file_manager = file_manager
        self.touch = touch
        self.display = display
        self.neo_pixel = neo_pixel
        self.game = game
        self.tarot = tarot
        self.bad_advice = bad_advice
        self.pair = pair
        self.demo = demo
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
        show_menu = True
        while True:
            if show_menu:
                self.__populate('game menu 1', 'l: tarot trivia', 'r: stego', 'u: re-enactment',
                                'd: scavenger hunt', 's: flash cards', 'e: main menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.__game_menu_tarot_trivia()
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.__game_menu_stego()
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                self.__game_menu_reenactment()
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                self.__game_menu_scavenger_hunt()
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                self.__game_menu_flash_cards()
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_tarot_trivia(self):
        """
        Private method to handle the tarot trivia game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('tarot trivia menu', 'l: instructions', 'r: practice', 'u: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.tarot_trivia_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.game.multiple_choice_practice(self.data.tarot_trivia_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                won_game = self.game.multiple_choice(self.data.tarot_trivia_game, '66', 3, 2)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_stego(self):
        """
        Private method to handle the stego game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('stego menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.stego_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                won_game = self.game.sequence(self.data.stego_game, '23', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_reenactment(self):
        """
        Private method to handle the reenactment game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('reenactment menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.reenactment_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                won_game = self.game.sequence(self.data.reenactment_game, '89', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_scavenger_hunt(self):
        """
        Private method to handle the scavenger hunt game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('scavenger hunt menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.scavenger_hunt_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                won_game = self.game.sequence(self.data.scavenger_hunt_game, '40', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_flash_cards(self):
        """
        Private method to handle the flash cards game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('flash cards menu', 'l: instructions', 'r: practice', 'u: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.flash_cards_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.game.multiple_choice_practice(self.data.flash_cards_game, text=False)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                won_game = self.game.multiple_choice(self.data.flash_cards_game, '98', 2, 1, text=False)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_2(self):
        """
        Private method to handle the game menu 2
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('game menu 2', 'l: fun deck', 'r: morse code', 'u: decryption',
                                'd: malort', 's: nfc', 'e: main menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.__game_menu_fun_deck()
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.__game_menu_morse_code()
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                self.__game_menu_decryption()
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                self.__game_menu_malort()
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                self.__game_menu_nfc()
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_fun_deck(self):
        """
        Private method to handle the fun deck game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('fun deck menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.fun_deck_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                won_game = self.game.sequence(self.data.fun_deck_game, '11', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                self.game.multiple_choice_practice(self.data.fun_deck_game)
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_morse_code(self):
        """
        Private method to handle the morse code game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('morse code menu', 'l: instructions', 'r: practice-easy',
                                'u: practice-medium', 'd: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.morse_code_game_instructions_1)
                self.display.text(self.data.morse_code_game_instructions_2)
                self.display.text(self.data.morse_code_game_instructions_3)
                self.display.text(self.data.morse_code_game_instructions_4)
                self.display.text(self.data.morse_code_game_instructions_5)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.game.morse_code_practice(self.data.morse_code_game_practice_easy)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                self.game.morse_code_practice(self.data.morse_code_game_practice_medium)
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                won_game = self.game.morse_code_sequence(self.data.morse_code_game, '15', 3, 3)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_decryption(self):
        """
        Private method to handle the decryption game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('decryption menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.decryption_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.display.text(self.data.decryption_game_setup['Instructions'])
                self.display.text(self.data.decryption_game_setup['Cipher 1'])
                self.display.text(self.data.decryption_game_setup['Cipher 2'])
                self.display.text(self.data.decryption_game_setup['Cipher 3'])
                self.display.text(self.data.decryption_game_setup['Submit'])
                won_game = self.game.sequence(self.data.decryption_game, '37', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_malort(self):
        """
        Private method to handle the malort game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('malort menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.malort_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                won_game = self.game.sequence(self.data.malort_game, '71', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_nfc(self):
        """
        Private method to handle the nfc game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('nfc menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.nfc_game_instructions)
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                won_game = self.game.sequence(self.data.nfc_game, '53', 1, 1)
                if won_game:
                    self.display.text('YOU WON!')
                    self.game.won(won_game)
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __tarot_reading_menu(self):
        """
        Private method to handle the tarot reading menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('tarot reading menu', 'l: instructions', 'r: choose deck', 'u: tarot reading',
                                'd: tarot scroll', 'e: main menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.tarot_instructions_1)
                self.display.text(self.data.tarot_instructions_2)
                self.display.text(self.data.tarot_instructions_3)
                show_menu = True
            if self.touch.press(self.touch.button_right):
                deck_selected = False
                try:
                    folders = uos.listdir('sd')
                    for folder in folders:
                        if folder == 'System Volume Information' or folder == '.fseventsd' or \
                                folder == '.Spotlight-V100' or folder == '.Trashes' or folder == 'bad_advice':
                            pass
                        else:
                            self.display.text(folder, timed=False)
                            while True:
                                if self.touch.press(self.touch.button_left):
                                    self.deck = folder
                                    self.file_manager.write_tarot_deck_folder(folder)
                                    self.display.text('DECK CHANGED')
                                    deck_selected = True
                                    break
                                elif self.touch.press(self.touch.button_right):
                                    break
                        if deck_selected:
                            break
                        show_menu = True
                except OSError:
                    # self.display.text('sd card is damaged')
                    show_menu = True
            elif self.touch.press(self.touch.button_up):
                self.tarot.reading()
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                self.tarot.scroll()
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __bad_advice_menu(self):
        """
        Private method to handle the bad advice menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('bad advice menu', 'l: bad advice scroll', 'e: main menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.bad_advice.scroll()
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __extras_menu(self):
        """
        Private method to handle the extras menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('extras menu', 'l: demo', 'r: badge reset', 'u: game 11/12 pair', 'd: pair',
                                'e: main menu')
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_left):
                self.demo.play()
                self.file_manager.update_games_won()
                show_menu = True
            elif self.touch.press(self.touch.button_right):
                self.file_manager.reset('games_won')
                show_menu = True
            elif self.touch.press(self.touch.button_up):
                self.display.text(self.data.pairing_games_instructions_1)
                self.display.text(self.data.pairing_games_instructions_2)
                show_menu = True
            elif self.touch.press(self.touch.button_down):
                self.pair.badge()
                show_menu = True
            elif self.touch.press(self.touch.button_submit):
                illumaniti_sequence = self.touch.numeric_sequence(show=True)
                if illumaniti_sequence == '33441212':
                    self.display.image('3Hats.raw',  timed=False)
                    while True:
                        self.neo_pixel.illuminati()
                        if self.touch.press(self.touch.button_left):
                            self.neo_pixel.clear(hard_clear=True)
                            self.file_manager.update_games_won()
                            break
                show_menu = True
            elif self.touch.press(self.touch.button_extra):
                break

    def __main_menu(self):
        """
        Private method to handle the main menu
        """
        self.__populate('main menu', 'l: instructions', 'r: games 1 menu', 'u: games 2 menu', 'd: tarot menu',
                        's: bad advice menu', 'e: extras menu')
        self.file_manager.update_games_won()
        while True:
            if self.touch.press(self.touch.button_left):
                self.display.text(self.data.badge_instructions_1)
                self.display.text(self.data.badge_instructions_2)
                self.display.text(self.data.badge_instructions_3)
                break
            elif self.touch.press(self.touch.button_right):
                self.__game_menu_1()
                break
            elif self.touch.press(self.touch.button_up):
                self.__game_menu_2()
                break
            elif self.touch.press(self.touch.button_down):
                self.__tarot_reading_menu()
                break
            elif self.touch.press(self.touch.button_submit):
                self.__bad_advice_menu()
                break
            elif self.touch.press(self.touch.button_extra):
                self.__extras_menu()
                break

    def system(self):
        """
        Method to handle the menu system
        """
        self.file_manager.update_games_won()
        while True:
            self.__main_menu()

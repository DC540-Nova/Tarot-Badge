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
        self.positon = None
        self.end_line = None
        self.clear_text = '                                                                                            '
        self.x_spacer = 32
        self.title = 8
        self.wait = 0.1
        self.line_2 = 32
        self.line_3 = 56
        self.line_4 = 80
        self.line_5 = 104
        self.line_6 = 128
        self.line_7 = 152
        self.line_8 = 176

    def __populate(self, title, line_3='', line_4='', line_5='', line_6='', line_7='', line_8='',
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
            title_color: int, optional
        """
        self.text = title
        self.display.text(self.text, y=self.title, color=title_color, wrap=False, clear=True, timed=False, off=True)
        self.text = line_3
        self.display.text(self.text, x=self.x_spacer, y=self.line_3, wrap=False, clear=False, timed=False, off=True)
        self.text = line_4
        self.display.text(self.text, x=self.x_spacer, y=self.line_4, wrap=False, clear=False, timed=False, off=True)
        self.text = line_5
        self.display.text(self.text, x=self.x_spacer, y=self.line_5, wrap=False, clear=False, timed=False, off=True)
        self.text = line_6
        self.display.text(self.text, x=self.x_spacer, y=self.line_6, wrap=False, clear=False, timed=False, off=True)
        self.text = line_7
        self.display.text(self.text, x=self.x_spacer, y=self.line_7, wrap=False, clear=False, timed=False, off=True)
        self.text = line_8
        self.display.text(self.text, x=self.x_spacer, y=self.line_8, wrap=False, clear=False, timed=False, off=False)

    def __deck_menu(self, all_folders, all_folders_len, text_upper_limit):
        """
        Private method to display decks
        """
        if all_folders_len == 1:
            self.__populate('decks', all_folders[0][:text_upper_limit])
        elif all_folders_len == 2:
            self.__populate('decks', all_folders[0][:text_upper_limit],
                            all_folders[1][:text_upper_limit])
        elif all_folders_len == 3:
            self.__populate('decks', all_folders[0][:text_upper_limit],
                            all_folders[1][:text_upper_limit],
                            all_folders[2][:text_upper_limit])
        elif all_folders_len == 4:
            self.__populate('decks', all_folders[0][:text_upper_limit],
                            all_folders[1][:text_upper_limit],
                            all_folders[2][:text_upper_limit],
                            all_folders[3][:text_upper_limit])
        elif all_folders_len == 5:
            self.__populate('decks', all_folders[0][:text_upper_limit],
                            all_folders[1][:text_upper_limit],
                            all_folders[2][:text_upper_limit],
                            all_folders[3][:text_upper_limit],
                            all_folders[4][:text_upper_limit])
        elif all_folders_len >= 6:
            self.__populate('decks', all_folders[0][:text_upper_limit],
                            all_folders[1][:text_upper_limit],
                            all_folders[2][:text_upper_limit],
                            all_folders[3][:text_upper_limit],
                            all_folders[4][:text_upper_limit],
                            all_folders[5][:text_upper_limit])

    def __up(self):
        """
        Private method to handle an up arrow action
        """
        if self.position > self.line_3:
            self.display.text('>', x=10, y=self.position, color=0b0000000000000000, wrap=False, clear=False,
                              timed=False, off=True)
            self.position -= 24
            self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
        sleep(self.wait)

    def __down(self):
        """
        Private method to handle a down arrow action
        """
        if self.position <= self.end_line:
            self.display.text('>', x=10, y=self.position, color=0b0000000000000000, wrap=False, clear=False,
                              timed=False, off=True)
            self.position += 24
            self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
        sleep(self.wait)

    def __game_menu_1(self):
        """
        Private method to handle the game menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('game menu 1', 'tarot trivia', 'stego', 're-enactment', 'scavenger hunt', 'flash cards',
                                'main menu')
                self.position = self.line_3
                self.end_line = self.line_7
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.__game_menu_tarot_trivia()
                    show_menu = True
                elif self.position == self.line_4:
                    self.__game_menu_stego()
                    show_menu = True
                elif self.position == self.line_5:
                    self.__game_menu_reenactment()
                    show_menu = True
                elif self.position == self.line_6:
                    self.__game_menu_scavenger_hunt()
                    show_menu = True
                elif self.position == self.line_7:
                    self.__game_menu_flash_cards()
                    show_menu = True
                elif self.position == self.line_8:
                    break

    def __game_menu_tarot_trivia(self):
        """
        Private method to handle the tarot trivia game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('tarot trivia menu', 'instructions', 'practice', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_5
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.tarot_trivia_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    self.game.multiple_choice_practice(self.data.tarot_trivia_game)
                    show_menu = True
                elif self.position == self.line_5:
                    won_game = self.game.multiple_choice(self.data.tarot_trivia_game, '66', 20, 15)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_6:
                    break

    def __game_menu_stego(self):
        """
        Private method to handle the stego game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('stego menu', 'instructions', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.stego_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    won_game = self.game.sequence(self.data.stego_game, '23', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_5:
                    break

    def __game_menu_reenactment(self):
        """
        Private method to handle the reenactment game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('reenactment menu', 'instructions', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.reenactment_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    won_game = self.game.sequence(self.data.reenactment_game, '89', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_5:
                    break

    def __game_menu_scavenger_hunt(self):
        """
        Private method to handle the scavenger hunt game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('scavenger hunt menu', 'instructions', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.scavenger_hunt_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    won_game = self.game.sequence(self.data.scavenger_hunt_game, '40', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_5:
                    break

    def __game_menu_flash_cards(self):
        """
        Private method to handle the flash cards game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('flash cards menu', 'instructions', 'practice', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_5
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.flash_cards_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    self.game.multiple_choice_practice(self.data.flash_cards_game, text=False)
                    show_menu = True
                elif self.position == self.line_5:
                    won_game = self.game.multiple_choice(self.data.flash_cards_game, '98', 20, 15, text=False)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_6:
                    break

    def __game_menu_2(self):
        """
        Private method to handle the game menu 2
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('game menu 2', 'fun deck', 'morse code', 'decryption', 'malort', 'nfc', 'main menu')
                self.position = self.line_3
                self.end_line = self.line_7
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.__game_menu_fun_deck()
                    show_menu = True
                elif self.position == self.line_4:
                    self.__game_menu_morse_code()
                    show_menu = True
                elif self.position == self.line_5:
                    self.__game_menu_decryption()
                    show_menu = True
                elif self.position == self.line_6:
                    self.__game_menu_malort()
                    show_menu = True
                elif self.position == self.line_7:
                    self.__game_menu_nfc()
                    show_menu = True
                elif self.position == self.line_8:
                    break

    def __game_menu_fun_deck(self):
        """
        Private method to handle the fun deck game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('fun deck menu', 'instructions', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.fun_deck_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    won_game = self.game.sequence(self.data.fun_deck_game, '11', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_5:
                    break

    def __game_menu_morse_code(self):
        """
        Private method to handle the morse code game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('morse code menu', 'instructions', 'practice-easy', 'practice-medium', 'play',
                                'prior menu')
                self.position = self.line_3
                self.end_line = self.line_6
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.morse_code_game_instructions_1)
                    self.display.text(self.data.morse_code_game_instructions_2)
                    self.display.text(self.data.morse_code_game_instructions_3)
                    self.display.text(self.data.morse_code_game_instructions_4)
                    self.display.text(self.data.morse_code_game_instructions_5)
                    show_menu = True
                elif self.position == self.line_4:
                    self.game.morse_code_practice(self.data.morse_code_game_practice_easy)
                    show_menu = True
                elif self.position == self.line_5:
                    self.game.morse_code_practice(self.data.morse_code_game_practice_medium)
                    show_menu = True
                elif self.position == self.line_6:
                    won_game = self.game.morse_code_sequence(self.data.morse_code_game, '15', 3, 3)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_7:
                    break

    def __game_menu_decryption(self):
        """
        Private method to handle the decryption game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('decryption menu', 'instructions', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.decryption_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    self.display.text(self.data.decryption_game_setup['Instructions'])
                    self.display.text(self.data.decryption_game_setup['Cipher 1'], sleep_time=12)
                    self.display.text(self.data.decryption_game_setup['Cipher 2'], sleep_time=12)
                    self.display.text(self.data.decryption_game_setup['Cipher 3'], sleep_time=12)
                    self.display.text(self.data.decryption_game_setup['Submit'])
                    won_game = self.game.sequence(self.data.decryption_game, '37', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_5:
                    break
            elif self.touch.press(self.touch.button_extra):
                break

    def __game_menu_malort(self):
        """
        Private method to handle the malort game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('malort menu', 'instructions', 'play', 'prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.malort_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    won_game = self.game.sequence(self.data.malort_game, '71', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_5:
                    break

    def __game_menu_nfc(self):
        """
        Private method to handle the nfc game
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('nfc menu', 'l: instructions', 'r: play', 'e: prior menu')
                self.position = self.line_3
                self.end_line = self.line_4
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.nfc_game_instructions)
                    show_menu = True
                elif self.position == self.line_4:
                    won_game = self.game.sequence(self.data.nfc_game, '53', 1, 1)
                    if won_game:
                        self.display.text('YOU WON!')
                        self.game.won(won_game)
                    show_menu = True
                elif self.position == self.line_4:
                    break

    def __tarot_reading_menu(self):
        """
        Private method to handle the tarot reading menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('tarot reading menu', 'instructions', 'choose deck', 'tarot reading', 'tarot scroll',
                                'main menu')
                self.position = self.line_3
                self.end_line = self.line_6
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.tarot_instructions_1)
                    self.display.text(self.data.tarot_instructions_2)
                    self.display.text(self.data.tarot_instructions_3)
                    show_menu = True
                elif self.position == self.line_4:
                    try:
                        folders = uos.listdir('sd')
                        all_folders = ''
                        for folder in folders:
                            if folder == 'System Volume Information' or folder.startswith('.') or \
                                    folder == 'bad_advice' or folder == '3Hats.raw' or folder == 'dc540_logo.raw' or \
                                    folder == 'Unispace12x24.c':
                                pass
                            else:
                                all_folders += folder + ' '
                        all_folders = all_folders.split()  # split the strings on a space
                        all_folders = list(all_folders)  # split out string of decks to a list
                        deck_order = []
                        seed = 0
                        for _ in all_folders:
                            deck_order.append(seed)
                            seed += 1
                        deck_order = deck_order[1:]
                        deck_order.append(0)
                        all_folders_len = len(all_folders)
                        # print(all_folders)
                        # print(all_folders_len)
                        text_upper_limit = 15
                        # print(all_folders)
                        # print(type(all_folders))
                        # print(len(all_folders))
                        self.__deck_menu(all_folders, all_folders_len, text_upper_limit)
                        self.position = self.line_3
                        self.end_line = ((all_folders_len - 2) * 24) + self.line_3
                        if self.end_line >= self.line_7:
                            self.end_line = self.line_7
                        if self.position == self.line_3:
                            self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False,
                                              off=True)
                        while True:
                            if self.touch.press(self.touch.button_up):
                                if all_folders_len > 6 and self.position == self.line_3:
                                    all_folders = [all_folders[i] for i in deck_order]
                                    self.__deck_menu(all_folders, all_folders_len, text_upper_limit)
                                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False,
                                                      off=True)
                                self.__up()
                            elif self.touch.press(self.touch.button_down):
                                if all_folders_len > 6 and self.position == self.line_8:
                                    all_folders = [all_folders[i] for i in deck_order]
                                    self.__deck_menu(all_folders, all_folders_len, text_upper_limit)
                                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False,
                                                      off=True)
                                self.__down()
                            elif self.touch.press(self.touch.button_submit):
                                if self.position == self.line_3:
                                    self.deck = all_folders[0]
                                    # print(all_folders[0])
                                    self.file_manager.write_tarot_deck_folder(all_folders[0])
                                    break
                                elif self.position == self.line_4:
                                    self.deck = all_folders[1]
                                    # print(all_folders[1])
                                    self.file_manager.write_tarot_deck_folder(all_folders[1])
                                    break
                                elif self.position == self.line_5:
                                    self.deck = all_folders[2]
                                    # print(all_folders[2])
                                    self.file_manager.write_tarot_deck_folder(all_folders[2])
                                    break
                                elif self.position == self.line_6:
                                    self.deck = all_folders[3]
                                    # print(all_folders[3])
                                    self.file_manager.write_tarot_deck_folder(all_folders[3])
                                    break
                                elif self.position == self.line_7:
                                    self.deck = all_folders[4]
                                    # print(all_folders[4])
                                    self.file_manager.write_tarot_deck_folder(all_folders[4])
                                    break
                                elif self.position == self.line_8:
                                    self.deck = all_folders[5]
                                    # print(all_folders[5])
                                    self.file_manager.write_tarot_deck_folder(all_folders[5])
                                    break
                        self.display.text('DECK CHANGED')
                        show_menu = True
                    except OSError:
                        # self.display.text('sd card is damaged')
                        show_menu = True
                elif self.position == self.line_5:
                    self.tarot.reading()
                    show_menu = True
                elif self.position == self.line_6:
                    self.tarot.scroll()
                    show_menu = True
                elif self.position == self.line_7:
                    break

    def __bad_advice_menu(self):
        """
        Private method to handle the bad advice menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('bad advice menu', 'bad advice scroll', 'main menu')
                self.position = self.line_3
                self.end_line = self.line_3
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.bad_advice.scroll()
                    self.file_manager.update_games_won()
                    show_menu = True
                elif self.position == self.line_4:
                    break

    def __extras_menu(self):
        """
        Private method to handle the extras menu
        """
        show_menu = True
        while True:
            if show_menu:
                self.__populate('extras menu', 'demo', 'badge reset', 'game 11/12 pair', 'pair', 'main menu')
                self.position = self.line_3
                self.end_line = self.line_6
                if self.position == self.line_3:
                    self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
                self.file_manager.update_games_won()
                show_menu = False
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.demo.play()
                    self.file_manager.update_games_won()
                    show_menu = True
                elif self.position == self.line_4:
                    self.file_manager.reset('games_won')
                    show_menu = True
                elif self.position == self.line_5:
                    self.display.text(self.data.pairing_games_instructions_1)
                    self.display.text(self.data.pairing_games_instructions_2)
                    show_menu = True
                elif self.position == self.line_6:
                    self.pair.badge()
                    show_menu = True
                elif self.position == self.line_7:
                    break
            elif self.touch.press(self.touch.button_extra):
                illumaniti_sequence = self.touch.numeric_sequence(show=True)
                if illumaniti_sequence == '33441212':
                    self.display.image('sd/3Hats.raw',  timed=False)
                    while True:
                        self.neo_pixel.illuminati()
                        if self.touch.press(self.touch.button_extra):
                            self.neo_pixel.clear(hard_clear=True)
                            self.file_manager.update_games_won()
                            break
                show_menu = True

    def __main_menu(self):
        """
        Private method to handle the main menu
        """
        self.__populate('main menu', 'instructions', 'games 1 menu', 'games 2 menu', 'tarot menu', 'bad advice menu',
                        'extras menu')
        self.position = self.line_3
        self.end_line = self.line_7
        if self.position == self.line_3:
            self.display.text('>', x=10, y=self.position, wrap=False, clear=False, timed=False, off=True)
        self.file_manager.update_games_won()
        while True:
            if self.touch.press(self.touch.button_up):
                self.__up()
            elif self.touch.press(self.touch.button_down):
                self.__down()
            elif self.touch.press(self.touch.button_submit):
                if self.position == self.line_3:
                    self.display.text(self.data.badge_instructions_1)
                    self.display.text(self.data.badge_instructions_2)
                    self.display.text(self.data.badge_instructions_3)
                    break
                elif self.position == self.line_4:
                    self.__game_menu_1()
                    break
                elif self.position == self.line_5:
                    self.__game_menu_2()
                    break
                elif self.position == self.line_6:
                    self.__tarot_reading_menu()
                    break
                elif self.position == self.line_7:
                    self.__bad_advice_menu()
                    break
                elif self.position == self.line_8:
                    self.__extras_menu()
                    break

    def system(self):
        """
        Method to handle the menu system
        """
        self.file_manager.update_games_won()
        while True:
            self.__main_menu()

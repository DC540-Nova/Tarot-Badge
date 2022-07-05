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


class Menu:
    """
    Base class to handle a menu system
    """

    def __init__(self, button, display, neo_pixel, game, tarot, data):
        """
        Params:
            button: object
            display: object
            neo_pixel: object
            game: object
            tarot: object
            data: object
        """
        self.button = button
        self.display = display
        self.neo_pixel = neo_pixel
        self.game = game
        self.tarot = tarot
        self.data = data
        self.text = None
        self.button_pressed = None

    def __game_menu_1(self):
        """
        Private method to handle the game menu
        """
        self.text = 'games 1'
        self.display.text(self.text, color=0b11001111011011111010001, timed=False, off=True)
        # self.text = 'L: tarot trivia R: stego  U: reenactment D: hunt   S: flash card E: main menu'
        self.display.text(self.text, y=48, wrap=False, clear=False, timed=False, off=True)

        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.__game_menu_tarot_trivia()
        elif self.button_pressed == 2:
            self.__game_menu_stego()
        elif self.button_pressed == 2:
            pass
        elif self.button_pressed == 6:
            self.__main_menu()

    def __game_menu_tarot_trivia(self):
        """
        Private method to handle the tarot trivia
        """
        self.text = 'tarot trivia'
        self.display.text(self.text, color=0b11001111011011111010001, timed=False, off=True)
        self.text = 'L: instructions R: play U: practice D: main menu'
        self.display.text(self.text, y=48, clear=False, timed=False)
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.display.text(self.data.tarot_trivia_instructions)
        elif self.button_pressed == 2:
            won_game = self.game.multiple_choice(self.data.tarot_trivia, '2', '1', 1, False)
            if won_game:
                self.game.won(won_game)
        elif self.button_pressed == 3:
            self.game.practice(self.data.tarot_trivia)
        elif self.button_pressed == 6:
            self.__main_menu()

    def __game_menu_stego(self):
        """
        Private method to handle the stego game
        """
        pass

    def __game_menu_2(self):
        """
        Private method to handle the game menu 2
        """
        self.text = 'games 2'
        self.display.text(self.text, color=0b11001111011011111010001, timed=False, off=True)
        self.text = 'L: fun deck R: morse code U: decryption D: boss pairing S: help me E: main menu'
        self.display.text(self.text, y=48, clear=False, timed=False)
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            won_game = self.game.multiple_choice(self.data.tarot_trivia, '1', 1)
            if won_game:
                self.game.won(won_game)
        elif self.button_pressed == 2:
            self.game.practice(self.data.tarot_trivia)
        elif self.button_pressed == 3:
            won_game = self.game.multiple_choice(self.data.flash_cards, '2', 1, False)
            if won_game:
                self.game.won(won_game)
        elif self.button_pressed == 4:
            self.game.practice(self.data.flash_cards)

    def __tarot_reading_menu(self):
        """
        Private method to handle the tarot reading
        """
        self.tarot.reading(self.data.cards)

    def __bad_advice_menu(self):
        """
        Private method to handle the bad advice menu
        """
        self.text = 'bad advice menu --------- L: tarot trivia  R: flash cards'
        self.display.text(self.text, timed=False)
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.game.multiple_choice_questions(self.data.tarot_trivia, '1', 2)
        elif self.button_pressed == 2:
            self.game.multiple_choice_questions(self.data.flash_cards, '2', 2)

    def __extras_menu(self):
        """
        Private method to handle the extras menu
        """
        self.text = 'extras menu --------- L: tarot trivia  R: flash cards'
        self.display.text(self.text, timed=False)
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.game.multiple_choice_questions(self.data.tarot_trivia, '1', 2)
        elif self.button_pressed == 2:
            self.game.multiple_choice_questions(self.data.flash_cards, '2', 2)

    def __main_menu(self):
        """
        Private method to handle the main menu
        """
        self.text = 'main menu'
        self.display.text(self.text, color=0b11001111011011111010001, timed=False, off=True)
        self.text = 'L: instructions R: games 1 U: games 2 D: tarot reading S: pair   E: extras'
        self.display.text(self.text, y=48, clear=False, timed=False)
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.display.text(self.data.instructions)
        elif self.button_pressed == 2:
            self.__game_menu_1()
        elif self.button_pressed == 3:
            self.__game_menu_2()
        elif self.button_pressed == 4:
            self.__tarot_reading_menu()
        elif self.button_pressed == 5:
            self.__bad_advice_menu()
        elif self.button_pressed == 6:
            self.__extras_menu()

    def system(self):
        """
        Method to handle the menu system
        """
        # self.display.image('dc540_logo.raw')
        while True:
            self.__main_menu()

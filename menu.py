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

    def __init__(self, button, display, neo_pixel, game, tarot, data, deck=1):
        """
        Params:
            button: object
            display: object
            neo_pixel: object
            game: object
            tarot: object
            data: object
            deck: int
        """
        self.button = button
        self.display = display
        self.neo_pixel = neo_pixel
        self.game = game
        self.tarot = tarot
        self.data = data
        self.deck = deck
        self.text = None
        self.button_pressed = None
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
        self.display.text(self.text, y=self.title, color=title_color, wrap=False, clear=True,
                          timed=False, off=True)
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
        self.__populate('game menu 1', 'l: tarot trivia', 'r: stego', 'u: re-enactment', 'd: hunt', 's: flash card',
                        'e: main menu')
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.__game_menu_tarot_trivia()
        elif self.button_pressed == 2:
            self.__game_menu_stego()
        elif self.button_pressed == 3:
            pass
        elif self.button_pressed == 4:
            pass
        elif self.button_pressed == 5:
            pass
        elif self.button_pressed == 6:
            self.__main_menu()

    def __game_menu_tarot_trivia(self):
        """
        Private method to handle the tarot trivia
        """
        self.__populate('tarot trivia', 'l: instructions', 'r: play', 'u: practice', 'd: main menu')
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.display.text(self.data.tarot_trivia_instructions)
        elif self.button_pressed == 2:
            won_game = self.game.multiple_choice(self.data.tarot_trivia, '2', '1', 1, False)
            if won_game:
                self.game.won(won_game)
        elif self.button_pressed == 3:
            self.game.practice(self.data.tarot_trivia)
        elif self.button_pressed == 4:
            self.__main_menu()
        elif self.button_pressed == 5:
            pass
        elif self.button_pressed == 6:
            pass

    def __game_menu_stego(self):
        """
        Private method to handle the stego game
        """
        pass

    def __game_menu_2(self):
        """
        Private method to handle the game menu 2
        """
        self.__populate('game menu 2', 'l: fun deck', 'r: morse code', 'u: decryption', 'd: boss paring', 's: help me',
                        'e: main menu')
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            pass
        elif self.button_pressed == 2:
            pass
        elif self.button_pressed == 3:
            pass
        elif self.button_pressed == 4:
            pass
        elif self.button_pressed == 5:
            pass
        elif self.button_pressed == 6:
            self.__main_menu()

    def __tarot_reading_menu(self):
        """
        Private method to handle the tarot reading menu
        """
        self.__populate('tarot reading menu', 'l: load deck 1', 'r: load deck 2', 'u: load deck 3',
                        'd: load deck 4', 's: tarot reading', 'e: main menu')
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            self.deck = 1
        elif self.button_pressed == 2:
            self.deck = 2
        elif self.button_pressed == 3:
            self.deck = 3
        elif self.button_pressed == 4:
            self.deck = 4
        elif self.button_pressed == 5:
            self.tarot.reading(self.deck)
        elif self.button_pressed == 6:
            self.__main_menu()

    def __bad_advice_menu(self):
        """
        Private method to handle the bad advice menu
        """
        self.__populate('bad advice menu', '', '', '', '', '', 'e: main menu')
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            pass
        elif self.button_pressed == 2:
            pass
        elif self.button_pressed == 3:
            pass
        elif self.button_pressed == 4:
            pass
        elif self.button_pressed == 5:
            pass
        elif self.button_pressed == 6:
            self.__main_menu()

    def __extras_menu(self):
        """
        Private method to handle the extras menu
        """
        self.__populate('extras menu', '', '', '', '', '', 'e: main menu')
        self.button_pressed = self.button.press()
        if self.button_pressed == 1:
            pass
        elif self.button_pressed == 2:
            pass
        elif self.button_pressed == 3:
            pass
        elif self.button_pressed == 4:
            pass
        elif self.button_pressed == 5:
            pass
        elif self.button_pressed == 6:
            self.__main_menu()

    def __main_menu(self):
        """
        Private method to handle the main menu
        """
        self.__populate('main menu', 'l: instructions', 'r: games 1 menu', 'u: games 2 menu', 'd: tarot reading',
                        's: bad advice menu', 'e: extras menu')
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
        self.display.image('dc540_logo.raw')
        while True:
            self.__main_menu()

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
# mpremote connect /dev/tty.u* cp main.py :
# mpremote connect /dev/tty.u* rm ili9341.py :
# mpremote connect /dev/tty.u* cp main.py :/sd/
# mpremote connect /dev/tty.u* cp *.* :/sd/
# mpremote connect /dev/tty.u* exec 'import main;main.img_test()'
# screen /dev/tty.u*

from config import display, neo_pixel, nrf, BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, \
    BUTTON_EXTRA

from button import Button
from demo import Demo
from menu import Menu
import game
import tarot
import data

button = Button(BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display)
demo = Demo(display, neo_pixel)
menu = Menu(display, neo_pixel, button, game, tarot, data)


if __name__ == '__main__':
    demo.play()
    menu.system()






# def sd_test():
#     """
#     Function to test sd card functionality
#     """
#     with open('sd/test01.txt', 'w') as f:
#         f.write('Hello, Baab!\r\n')
#         f.write('This is the United States calling are we reaching?\r\n')
#     with open('sd/test01.txt', 'r') as f:
#         data = f.read()
#         print(data)







#game.morse_code(data.morse_code_practice_easy)




# game_number = game.multiple_choice_questions(data.flash_cards, '01', 2, image=True)
# file_manager.write_games_won_file(game_number)


# game_won = game.multiple_choice_questions(data.tarot_trivia, '02', 1, practice=False)
# print(game_won)
# if game_won:
#     game.won(game_won)




# create fake instruction placeholder (press button to advance)
# build out tarot trivia and flash cards for betsy next time we meet and demo it
# game_won = game.multiple_choice_questions(data.flash_cards, '01', 2, image=True)
# if game_won:
#     game.won(game_won)
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

import random

from config import button, display
from data import ham_radio_questions


def reading(card_bank):
    """
    Function to handle a tarot reading

    Params:
        card_bank, dict
    """
    reading = list(card_bank)  # noqa
    # reading_number = 0
    counter = 1
    for _ in card_bank:
        card_name, card_reading = random.choice(list(card_bank.items()))
        meaning = random.randint(1, 2)  # randomize card up or down position
        if meaning == 1:
            display.image('sd/' + card_reading[2])
        elif meaning == 2:
            display.image('sd/' + card_reading[2], up=False)
        if meaning == 1:
            display.text(card_reading[0])
        elif meaning == 2:
            display.text(card_reading[1])
        #correct_answer_index = answers[4]
        # strip off correct_answer_index from being displayed
    #     answers = answers[0:-1]
    #     for answer in answers:
    #         display.text(answer)
    #     answer = button.press()
    #     if answer == correct_answer_index:
    #         answer_list.append(1)
    #         display.text('CORRECT')
    #     else:
    #         answer_list.append(0)
    #         display.text('INCORRECT')
    #     question_number += 1
    #     counter += 1
    #     del ham_radio_questions[question]
    #     if counter > 5:
    #         break
    # answer_total = 0
    # for answer in answer_list:
    #     if answer == 1:
    #         answer_total += 1
    #     else:
    #         pass
    # if answer_total >= 2:
    #     return True
    # else:
    #     return False

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

import button_input
from neo_pixel import NeoPixel
from config import *
from data import *

neo_pixel = NeoPixel(Pin)


def questions(question_bank):
    """
    Function to handle a generic question loop

    Params:
        question_bank, dict

    Returns:
        bool
    """
    questions = list(question_bank)  # noqa
    question_number = 0
    counter = 1
    answer_list = []
    for _ in questions:
        question, answers = random.choice(list(ham_radio_questions.items()))
        display.draw_text(question)
        correct_answer_index = answers[4]
        # strip off correct_answer_index from being displayed
        answers = answers[0:-1]
        for answer in answers:
            display.draw_text(answer)
        display.draw_text('CHOOSE...')
        answer = button_input.get_response()
        if answer == correct_answer_index:
            answer_list.append(1)
            display.draw_text('CORRECT')
        else:
            answer_list.append(0)
            display.draw_text('INCORRECT')
        question_number += 1
        counter += 1
        del ham_radio_questions[question]
        if counter > 5:
            break
    answer_total = 0
    for answer in answer_list:
        if answer == 1:
            answer_total += 1
        else:
            pass
    if answer_total >= 2:
        return True
    else:
        return False

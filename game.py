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

import urandom  # noqa
from utime import sleep

from button_input import ButtonInput
import file_manager
from neo_pixel import NeoPixel
from ili9341 import color565

from config import *
from data import *

button_input = ButtonInput()
neo_pixel = NeoPixel(Pin)


def __ham_radio_question_loop(sleep_time=2):
    """
    Private function to handle ham radio question loop

    Params:
        sleep_time: int, optional

    Returns:
        bool
    """
    questions = list(ham_radio_questions)
    answers = list(ham_radio_questions.values())
    question_number = 0
    counter = 1
    answer_list = []
    for _ in questions:
        question, answers = urandom.choice(list(ham_radio_questions.items()))

        display.clear()
        display.draw_text(question, color565(255, 255, 0), unispace)
        display_on.value(1)
        correct_answer_index = answers[4]
        # strip off correct_answer_index from being displayed
        answers = answers[0:-1]
        sleep(sleep_time)
        for answer in answers:
            display.scroll_text([[0, 0, answer]], len(answer))
            sleep(sleep_time)
        answer = button_input.get_response(input_type='multiple_choice_letters')
        if answer == 'A':
            answer = 0
        elif answer == 'B':
            answer = 1
        elif answer == 'C':
            answer = 2
        else:
            answer = 3
        if answer == correct_answer_index:
            answer_list.append(1)
        else:
            answer_list.append(0)
        question_number += 1
        counter += 1
        del ham_radio_questions[question]
        if counter > 20:
            break
    answer_total = 0
    for answer in answer_list:
        if answer == 1:
            answer_total += 1
        else:
            pass
    if answer_total >= 15:
        return True
    else:
        return False

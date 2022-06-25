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

from config import display
import file_manager
import button


def multiple_choice_questions(question_bank, game_number, num_questions_to_win, image=False, practice=False):
    """
    Function to handle a generic multiple choice question loop

    Params:
        question_bank, dict
        game_number: str
        num_questions_to_win: int
        image: bool, optional
        practice: bool, optional

    Returns:
        str or bool
    """
    questions = list(question_bank)  # noqa
    question_number = 0
    counter = 0
    answer_list = []
    for _ in questions:
        question, answers = random.choice(list(question_bank.items()))
        if not image:
            display.text(question)
        elif image:
            display.image('sd/' + question)
        correct_answer_index = answers[4]
        answers = answers[0:-1]   # strip off correct_answer_index from being displayed
        for answer in answers:
            display.text(answer)
        display.text('CHOOSE...')
        answer = button.multiple_choice()
        if not practice:
            counter += 1
            if counter == num_questions_to_win:
                break
        if answer == correct_answer_index:
            if not practice:
                answer_list.append(1)
            elif practice:
                display.text('CORRECT')
        else:
            if not practice:
                answer_list.append(0)
            elif practice:
                display.text('INCORRECT')
        question_number += 1
        del question_bank[question]
        if practice:
            display.text('Would you like to practice with another question? ')
            display.text('CHOOSE...')
            response = button.yes_no()
            if response == 'yes':
                pass
            elif response != 'yes':
                return
    answer_total = 0
    for answer in answer_list:
        if answer == 1:
            answer_total += 1
        else:
            pass
    if answer_total >= num_questions_to_win:
        return game_number + ' '
    else:
        return False


def morse_code(question_bank):
    """

    """
    questions = list(question_bank)  # noqa
    question_number = 0
    counter = 0
    answer_list = []
    for _ in questions:
        question, answers = random.choice(list(question_bank.items()))
        display.text(question)
        correct_answer_index = answers[0]
        # answers = answers[0:-1]   # strip off correct_answer_index from being displayed
        # for answer in answers:
        #     display.text(answer)
        display.text('CHOOSE...')
        answer = button.morse_code()
        if answer == correct_answer_index:
            # do something to advance
            pass


def won(game_won):
    """
    Function to handle a single game win

    Params:
        game_won: int
    """
    games_won = file_manager.read_games_won_file()
    games_won += game_won
    file_manager.write_games_won_file(games_won)
    # TEMP FOR TESTING
    games_won = file_manager.read_games_won_file()
    print(games_won)

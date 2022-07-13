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


class Game:
    """
    Base class to handle a game
    """

    def __init__(self, button, file_manager, display, tarot):
        """
        Params:
            button: object
            file_manager: object
            display: object
            tarot: object

        """
        self.button = button
        self.file_manager = file_manager
        self.display = display
        self.tarot = tarot

    def multiple_choice(self, question_bank, game_number, num_questions, num_questions_to_win, text=True):
        """
        Method to handle a generic multiple choice question loop

        Params:
            question_bank: dict
            game_number: str
            num_questions: int
            num_questions_to_win: int
            text: bool, optional

        Returns:
            str or bool
        """
        questions = list(question_bank)
        question_number = 0
        counter = 0
        answer_list = []
        for _ in questions:
            question, answers = random.choice(list(question_bank.items()))
            if text:
                self.display.text(question)
            else:
                try:
                    self.display.image('sd/' + self.tarot.deck + '/' + question)
                except OSError:
                    self.display.text('please re-copy files to sd')
                    break
            correct_answer_index = answers[4]
            answers = answers[0:-1]   # strip off correct_answer_index from being displayed
            for answer in answers:
                self.display.text(answer)
            self.display.text('CHOOSE...')
            answer = self.button.multiple_choice()
            counter += 1
            if answer == correct_answer_index:
                answer_list.append(1)
            else:
                answer_list.append(0)
            question_number += 1
            del question_bank[question]
            answer_total = 0
            for answer in answer_list:
                if answer == 1:
                    answer_total += 1
                else:
                    pass
            if counter == num_questions:
                if answer_total >= num_questions_to_win:
                    return game_number + ' '
                else:
                    return False

    def practice(self, question_bank, text=True):
        """
        Method to handle practicing a generic multiple choice question loop

        Params:
            question_bank: dict
            test: bool, optional
        """
        questions = list(question_bank)
        for _ in questions:
            question, answers = random.choice(list(question_bank.items()))
            if text:
                self.display.text(question)
            else:
                try:
                    self.display.image('sd/' + self.tarot.deck + '/' + question)
                except OSError:
                    self.display.text('please re-copy files to sd')
                    break
            correct_answer_index = answers[4]
            answers = answers[0:-1]   # strip off correct_answer_index from being displayed
            for answer in answers:
                self.display.text(answer)
            self.display.text('CHOOSE...')
            answer = self.button.multiple_choice()
            if answer == correct_answer_index:
                self.display.text('CORRECT')
            else:
                self.display.text('INCORRECT')
            self.display.text('Would you like to practice with another question? ')
            self.display.text('CHOOSE...')
            response = self.button.yes_no()
            if response == 'yes':
                pass
            else:
                return

    def won(self, game_won):
        """
        Method to handle a single game win

        Params:
            game_won: str
        """
        games_won = self.file_manager.read_games_won_file()
        games_won += game_won
        self.file_manager.write_games_won_file(games_won)
        self.file_manager.update_games_won()

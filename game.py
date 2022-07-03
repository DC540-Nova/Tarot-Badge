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

    def __init__(self, display, file_manager, button, question_bank, game_number, num_questions_to_win, image=False,
                 practice=False):
        """
        Params:
            display: object
            button: object
            file_manager: object
            question_bank: dict
            game_number: str
            num_questions_to_win: int
            image: bool, optional
            practice: bool, optional
        """
        self.display = display
        self.button = button
        self.file_manager = file_manager
        self.question_bank = question_bank
        self.game_number = game_number
        self.num_questions_to_win = num_questions_to_win
        self.image = image
        self.practice = practice

    def multiple_choice_questions(self):
        """
        Method to handle a generic multiple choice question loop

        Returns:
            str or bool
        """
        questions = list(self.question_bank)
        question_number = 0
        counter = 0
        answer_list = []
        for _ in questions:
            question, answers = random.choice(list(self.question_bank.items()))
            if not self.image:
                self.display.text(question)
            elif self.image:
                self.display.image('sd/' + question)
            correct_answer_index = answers[4]
            answers = answers[0:-1]   # strip off correct_answer_index from being displayed
            for answer in answers:
                self.display.text(answer)
            self.display.text('CHOOSE...')
            answer = self.button.multiple_choice()
            if not self.practice:
                counter += 1
                if counter == self.num_questions_to_win:
                    break
            if answer == correct_answer_index:
                if not self.practice:
                    answer_list.append(1)
                elif self.practice:
                    self.display.text('CORRECT')
            else:
                if not self.practice:
                    answer_list.append(0)
                elif self.practice:
                    self.display.text('INCORRECT')
            question_number += 1
            del self.question_bank[question]
            if self.practice:
                self.display.text('Would you like to practice with another question? ')
                self.display.text('CHOOSE...')
                response = self.button.yes_no()
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
        if answer_total >= self.num_questions_to_win:
            return self.game_number + ' '
        else:
            return False

    # def morse_code(self):
    #     """
    #     Method to handle a morse code question loop
    #
    #     Returns:
    #         str or bool
    #     """

    def won(self):
        """
        Method to handle a single game win

        Params:
            game_won: int
        """
        games_won = self.file_manager.read_games_won_file()
        games_won += self.game_number
        self.file_manager.write_games_won_file(games_won)

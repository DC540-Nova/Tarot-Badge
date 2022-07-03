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

from data import boss_ids, boss_names
from config import display, neo_pixel, nrf, BLUE, GREEN
import microcontroller
import file_manager
import morse_code

# TODO: make class

def boss_send_id():
    """
    Method to check for a boss id and if they are a boss, send id
    """
    my_id_hex = microcontroller.get_unique_id()
    for id in boss_ids:  # noqa
        if my_id_hex == id:
            nrf.send(my_id_hex)
            break


def check_for_boss():
    """
    Method to check for a boss badge
    """
    display.text('Scanning...')
    foreign_unique_id = nrf.recv()
    foreign_unique_id = str(foreign_unique_id)
    # there is an edge case where some NRF modules are appending the last char of their own
    # unique_id to the beginning of the foreign_unique_id string
    if len(foreign_unique_id) == 17:
        foreign_unique_id = foreign_unique_id[1:]
    boss_names_index = 0
    for id in boss_ids:  # noqa
        if foreign_unique_id == id:
            display.text(boss_names[boss_names_index])
            morse_code.display('SOS')
            break
        boss_names_index += 1


def badge():
    """
    Method to pair badges
    """
    foreign_unique_id = None  # noqa
    display.text('Pairing...')
    unique_id = microcontroller.get_unique_id()
    nrf.send(unique_id)
    foreign_unique_id = nrf.recv()
    nrf.send(unique_id)
    # try again 2 times to ensure the pairing is successful
    for _ in range(2):
        if not foreign_unique_id:
            foreign_unique_id = nrf.recv()
        nrf.send(unique_id)
    if foreign_unique_id:
        foreign_unique_id = str(foreign_unique_id)
        # there is an edge case where some NRF modules are appending the last char of their own
        # unique_id to the beginning of the foreign_unique_id string
        if len(foreign_unique_id) == 17:
            foreign_unique_id = foreign_unique_id[1:]
        if foreign_unique_id[0] == 'e' and len(foreign_unique_id) == 16:
            ids = file_manager.read_ids_file()
            ids = list(ids.split(' '))
            ids = ids[0:-1]
            if ids:
                for id in ids:  # noqa
                    if id == foreign_unique_id:
                        neo_pixel.flicker(color=BLUE)
                        break
                    else:
                        neo_pixel.flicker(color=GREEN)
                        ids.append(foreign_unique_id)
                        ids = ['{} '.format(element) for element in ids]
                        str_ids = ''
                        for element in ids:
                            str_ids += element
                        file_manager.write_ids_file(str_ids)
                        break
                boss_names_index = 0
                for id in boss_ids:  # noqa
                    if foreign_unique_id == id:
                        display.scroll_text([[0, 0, boss_names[boss_names_index]]],
                                            len(boss_names[boss_names_index]))
                        neo_pixel.morse_code(sos, clear_display=False, encrypted=False)
                        break
                    boss_names_index += 1
            else:
                neo_pixel.flicker(color=GREEN)
                ids.append(foreign_unique_id)
                ids = ['{} '.format(element) for element in ids]
                str_ids = ''
                for element in ids:
                    str_ids += element
                file_manager.write_ids_file(str_ids)
                boss_names_index = 0
                for id in boss_ids:  # noqa
                    if foreign_unique_id == id:
                        display.scroll_text([[0, 0, boss_names[boss_names_index]]],
                                            len(boss_names[boss_names_index]))
                        neo_pixel.morse_code(sos, clear_display=False, encrypted=False)
                        break
                    boss_names_index += 1

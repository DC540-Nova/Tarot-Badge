# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
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


class Pair:
    """
    Base class to handle badge pairing
    """

    def __init__(self, microcontroller, file_manager, display, neo_pixel, morse_code, nrf, data):
        """
        Params:
            microcontroller: object
            file_manager: object
            display: object
            neo_pixel: object
            morse_code: object
            nrf: object
            data: dict
        """
        self.microcontroller = microcontroller
        self.file_manager = file_manager
        self.display = display
        self.neo_pixel = neo_pixel
        self.morse_code = morse_code
        self.nrf = nrf
        self.data = data

    def badge(self):
        """
        Method to pair badges
        """
        foreign_unique_id = None
        self.display.text('pairing...')
        unique_id = self.microcontroller.get_unique_id()
        # try 3 times to ensure the pairing is successful
        for _ in range(3):
            foreign_unique_id = self.nrf.recv()
            self.nrf.send(unique_id)
        if foreign_unique_id:
            foreign_unique_id = str(foreign_unique_id)
            # there is an edge case where some NRF modules are appending the last char of their own
            # unique_id to the beginning of the foreign_unique_id string
            if len(foreign_unique_id) == 17:
                foreign_unique_id = foreign_unique_id[1:]
            if foreign_unique_id[0] == 'e' and len(foreign_unique_id) == 16:
                ids = self.file_manager.read_ids_file()
                ids = list(ids.split(' '))
                ids = ids[0:-1]
                if ids:
                    for id in ids:  # noqa
                        if id == foreign_unique_id:
                            self.neo_pixel.flicker(color=self.neo_pixel.BLUE)
                            break
                        else:
                            self.neo_pixel.flicker(color=self.neo_pixel.GREEN)
                            ids.append(foreign_unique_id)
                            ids = ['{} '.format(element) for element in ids]
                            str_ids = ''
                            for element in ids:
                                str_ids += element
                            self.file_manager.write_ids_file(str_ids)
                            break
                    boss_names_index = 0
                    for id in boss_ids:  # noqa
                        if foreign_unique_id == id:
                            self.display.text(self.data.boss_names[boss_names_index])
                            self.morse_code.display('SOS')
                            break
                        boss_names_index += 1
                else:
                    self.neo_pixel.flicker(color=self.neo_pixel.GREEN)
                    ids.append(foreign_unique_id)
                    ids = ['{} '.format(element) for element in ids]
                    str_ids = ''
                    for element in ids:
                        str_ids += element
                    self.file_manager.write_ids_file(str_ids)
                    boss_names_index = 0
                    for id in boss_ids:  # noqa
                        if foreign_unique_id == id:
                            self.display.text(self.data.boss_names[boss_names_index])
                            self.morse_code.display('SOS')
                            break
                        boss_names_index += 1

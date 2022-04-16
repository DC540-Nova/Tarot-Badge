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

import sys
import os
from pathlib import Path
from PIL import Image
from PIL.Image import Resampling  # noqa


def error(msg):
    """
    Function to display error and exit

    Params:
        msg: str
    """
    print(msg)
    sys.exit(-1)


def convert(f):
    """
    Function to convert file to proper format for display

    Params:
        f: str
    """
    img = Image.open(f)
    new_width = 240
    new_height = 320
    img = img.resize((new_width, new_height), Resampling.LANCZOS)
    img.save(f)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 1:
        error('usage: python convert.py')

    directory = 'deck'
    if not os.path.exists(directory):  # noqa
        error('directory does not exist: ' + directory)

    files = Path(directory).glob('*')
    for filename in files:
        filename, ext = os.path.splitext(filename)  # noqa
        convert(filename + ext)
        print('saved: ' + filename + ext)

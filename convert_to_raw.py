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

import sys
import os
from PIL import Image
from struct import pack
from pathlib import Path


def error(msg):
    """
    Function to display error and exit
    
    Params:
        msg: str
    """
    print(msg)
    sys.exit(-1)


def write_bin(f, pixel_list):  # noqa
    """
    Method to save image in RGB565 format
    
    Params:
        f: object
        pixel_list: list
    """
    for pix in pixel_list:
        r = (pix[0] >> 3) & 0x1F
        g = (pix[1] >> 2) & 0x3F
        b = (pix[2] >> 3) & 0x1F
        f.write(pack('>H', (r << 11) + (g << 5) + b))
        

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        error('usage: python convert_to_raw.py')

    directory = args[1]
    if not os.path.exists(directory):  # noqa
        error('directory does not exist: ' + directory)

    new_directory = ''
    new_directory = os.path.abspath(new_directory) # noqa
    new_directory += '/'
    try:
        os.mkdir(Path(new_directory))
    except OSError as error:
        pass
    files = Path(directory).glob('*')
    for filename in files:
        filename, ext = os.path.splitext(filename)  # noqa
        absolute_path = os.path.abspath(__file__)  # noqa
        out_path = new_directory + filename + '.raw'  # noqa
        try:
            img = Image.open(filename + ext).convert('RGB')
            pixels = list(img.getdata())
            with open(out_path, 'wb') as f:
                write_bin(f, pixels)
            print('saved: ' + out_path)
        except:  # noqa
            pass

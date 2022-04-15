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

import array
from utime import sleep_ms, sleep
import rp2

from config import *


class NeoPixel:
    """
    Class to handle NeoPixel functionality
    """

    def __init__(self, pin, LED_COUNT=LED_COUNT):
        """
        Params:
            pin: object
            LED_COUNT: int
        """
        # create the StateMachine with the ws2812 program, outputting on Pin(LED_PIN)
        sm = rp2.StateMachine(0, self.__ws2812, freq=8_000_000, sideset_base=pin(LED_PIN))
        # start the StateMachine, it will wait for data on its FIFO
        sm.active(1)
        # display a pattern on the LEDs via an array of LED RGB values
        ar = array.array('I', [0 for _ in range(LED_COUNT)])
        self.num_leds = LED_COUNT
        self.sm = sm
        self.ar = ar
        self.spheres = [31, 27, 25, 20, 18, 15, 7, 9, 4, 0]
        self.paths = [28, 30, 29, 26, 22, 21, 23, 24, 19, 14, 13, 16, 17, 12, 11, 10, 8, 6, 3, 5, 2, 1]

    @staticmethod
    @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT,
                 autopull=True, pull_thresh=24)
    def __ws2812():
        """
        Internal method to handle ARM 32 assembly LED NeoPixel driver
        """
        T1 = 2
        T2 = 5
        T3 = 3
        wrap_target()
        label("bitloop")
        out(x, 1).side(0)[T3 - 1]
        jmp(not_x, "do_zero").side(1)[T1 - 1]
        jmp("bitloop").side(1)[T2 - 1]
        label("do_zero")
        nop().side(0)[T2 - 1]
        wrap()

    def pixels_set(self, led, color):
        """
        Method to set 24-bit color on pixel
        Params:
            led: int
            color: tuple
        """
        self.ar[led] = (color[1] << 16) + (color[0] << 8) + color[2]  # set 24-bit color

    def pixels_show(self, brightness=1):
        """
        Method to handle illumination of pixels
        Params:
            brightness: float, optional
        """
        dimmer_ar = array.array('I', [0 for _ in range(self.num_leds)])
        for ii, cc in enumerate(self.ar):
            r = int(((cc >> 8) & 0xFF) * brightness)  # 8-bit red dimmed to brightness
            g = int(((cc >> 16) & 0xFF) * brightness)  # 8-bit green dimmed to brightness
            b = int((cc & 0xFF) * brightness)  # 8-bit blue dimmed to brightness
            dimmer_ar[ii] = (g << 16) + (r << 8) + b  # 24-bit color dimmed to brightness
        self.sm.put(dimmer_ar, 8)  # update the state machine with new colors
        sleep_ms(10)

    def led_clear(self, reverse=False, hard_clear=False, clear_only_spheres=False, clear_only_paths=False):
        """
        Method to clear pixels

        Params:
            reverse: bool, optional
            hard_clear: bool, optional
            clear_only_spheres: bool, optional
            clear_only_paths: bool, optional
        """
        if hard_clear:
            for led in range(self.num_leds):
                self.pixels_set(led, BLACK)
            self.pixels_show()
        if clear_only_spheres:
            for led in self.spheres:
                self.pixels_set(led, BLACK)
                self.pixels_show()
        if clear_only_paths:
            for led in self.paths:
                self.pixels_set(led, BLACK)
                self.pixels_show()
        if reverse:
            for led in reversed(range(self.num_leds)):
                self.pixels_set(led, BLACK)
                self.pixels_show()
        else:
            for led in range(self.num_leds):
                self.pixels_set(led, BLACK)
                self.pixels_show()

    def led_on(self, led, color=RED, all_on=False, brightness=1.0):
        """
        Method to handle a pixels_set and pixels_show action all in one

        Params:
            led: int
            color: tuple, optional
            all_on: bool, optional
            brightness: float, optional
        """
        if all_on:
            for led in range(self.num_leds):
                self.pixels_set(led, color)
            self.pixels_show()
        else:
            self.pixels_set(led, color)
            self.pixels_show(brightness)

    def breathing_led_on(self, led, color=RED, repeat=1):
        """
        Method to handle a breathing led on animation
        Params:
            led: int
            color: tuple, optional
            repeat: int, optional
        """
        while repeat > 0:
            self.led_clear()
            step = 5
            breath_amps = [ii for ii in range(0, 1000, step)]
            breath_amps.extend([ii for ii in range(1000, -1, -step)])
            for ii in breath_amps:
                self.pixels_set(led, color)
                self.pixels_show(ii / 255)
                sleep(0.02)
            repeat -= 1

    def morse_code(self, sentence, color=RED, clear_display=True, encrypted=True):
        """
        Method to display a morse code animation
        Params:
            sentence: str
            color: tuple, optional
            clear_display: bool, optional
            encrypted: bool, optional
        """
        if clear_display:
            display.clear()
        self.led_clear()
        encoded_sentence = morse_code.convert_to_morse_code(sentence, encrypted)
        for letter in encoded_sentence:
            if letter == '.':
                morse_code.morse_code_dot(color)
            elif letter == '-':
                morse_code.morse_code_dash(color)
            else:
                morse_code.morse_code_pause()
        display.clear()
        file_manager.update_status()

    def flicker(self, color=RED, repeat=1):
        """
        Method to display a flicker animation
        Params:
            color: tuple, optional
            repeat: int, optional
        """
        display.clear()
        while repeat > 0:
            step = 5
            breath_amps = [ii for ii in range(0, 1000, step)]
            breath_amps.extend([ii for ii in range(10, -1, -step)])
            for ii in breath_amps:
                for led in self.spheres:
                    self.pixels_set(led, color)
                for led in self.paths:
                    self.pixels_set(led, color)
                self.pixels_show(ii / 25)
            repeat -= 1
        self.led_clear()
        display.clear()
        file_manager.update_status()

    def won(self, color=RED, repeat=5):
        """
        Method to display a won game animation
        Params:
            color: tuple, optional
            repeat: int, optional
        """
        while repeat > 0:
            step = 5
            breath_amps = [ii for ii in range(0, 10000, step)]
            breath_amps.extend([ii for ii in range(10000, -1, -step)])
            for ii in breath_amps:
                for led in self.spheres:
                    self.pixels_set(led, color)
                for led in self.paths:
                    self.pixels_set(led, color)
                self.pixels_show(ii / 25)
            repeat -= 1
        self.led_clear()
        display.clear()
        file_manager.update_status()
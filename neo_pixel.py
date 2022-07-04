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


class NeoPixel:
    """
    Class to handle NeoPixel functionality
    """

    # neopixel colors
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)
    WHITE = (255, 255, 255)
    BROWN = (165, 42, 42)
    ORANGE = (255, 65, 0)
    GRAY = (128, 128, 128)
    COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, BROWN, ORANGE, GRAY)

    def __init__(self, pin, led_pin, led_count):  # noqa
        """
        Params:
            pin: object
            led_pin: int
            led_count: int
        """
        # create the StateMachine with the ws2812 program, outputting on Pin(led_pin)
        sm = rp2.StateMachine(0, self.__ws2812, freq=8_000_000, sideset_base=pin(led_pin))  # noqa
        # start the StateMachine, it will wait for data on its FIFO
        sm.active(1)  # noqa
        # display a pattern on the LEDs via an array of LED RGB values
        ar = array.array('I', [0 for _ in range(led_count)])
        self.num_leds = led_count
        self.sm = sm
        self.ar = ar
        self.spheres = [31, 27, 25, 20, 18, 15, 7, 9, 4, 0]
        self.paths = [28, 30, 29, 26, 22, 21, 23, 24, 19, 14, 13, 16, 17, 12, 11, 10, 8, 6, 3, 5, 2, 1]

    @staticmethod
    @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)  # noqa
    def __ws2812():
        """
        Private method to handle ARM32 assembly LED neopixel driver
        """
        T1 = 2  # noqa
        T2 = 5  # noqa
        T3 = 3  # noqa
        wrap_target()  # noqa
        label("bitloop")  # noqa
        out(x, 1).side(0)[T3 - 1]  # noqa
        jmp(not_x, "do_zero").side(1)[T1 - 1]  # noqa
        jmp("bitloop").side(1)[T2 - 1]  # noqa
        label("do_zero")  # noqa
        nop().side(0)[T2 - 1]  # noqa
        wrap()  # noqa

    def __set(self, led, color):
        """
        Private method to set 24-bit color set neopixel

        Params:
            led: int
            color: tuple
        """
        self.ar[led] = (color[1] << 16) + (color[0] << 8) + color[2]  # set 24-bit color

    def __show(self, brightness=1):
        """
        Private method to show 24-bit color show neopixel

        Params:
            brightness: float, optional
        """
        dimmer_ar = array.array('I', [0 for _ in range(self.num_leds)])
        for ii, cc in enumerate(self.ar):
            red = int(((cc >> 8) & 0xFF) * brightness)  # 8-bit red dimmed to brightness
            green = int(((cc >> 16) & 0xFF) * brightness)  # 8-bit green dimmed to brightness
            blue = int((cc & 0xFF) * brightness)  # 8-bit blue dimmed to brightness
            dimmer_ar[ii] = (green << 16) + (red << 8) + blue  # 24-bit color dimmed to brightness
        self.sm.put(dimmer_ar, 8)  # update the state machine with new colors  # noqa
        sleep_ms(10)

    def clear(self, reverse=False, hard_clear=False, clear_only_spheres=False, clear_only_paths=False):
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
                self.set(led, self.BLACK)
            self.show()
        if clear_only_spheres:
            for led in self.spheres:
                self.set(led, self.BLACK)
                self.show()
        if clear_only_paths:
            for led in self.paths:
                self.set(led, self.BLACK)
                self.show()
        if reverse:
            for led in reversed(range(self.num_leds)):
                self.set(led, BLACK)
                self.show()
        else:
            for led in range(self.num_leds):
                self.set(led, self.BLACK)
                self.show()

    def on(self, led, color=RED, all_on=False, brightness=1.0):
        """
        Method to handle a set and show neopixel action all in one

        Params:
            led: int
            color: tuple, optional
            all_on: bool, optional
            brightness: float, optional
        """
        if all_on:
            for led in range(self.num_leds):
                self.__set(led, color)
            self.__show()
        else:
            self.__set(led, color)
            self.__show(int(brightness))

    def off(self, led, color=BLACK, brightness=1.0):
        """
        Method to handle a clear of an individual neo pixel

        Params:
            led: int
            color: tuple, optional
            brightness: float, optional
        """
        self.__set(led, color)
        self.__show(int(brightness))

    def flicker(self, color=RED, repeat=1):
        """
        Method to display a flicker animation

        Params:
            color: tuple, optional
            repeat: int, optional
        """
        while repeat > 0:
            step = 5
            breath_amps = [ii for ii in range(0, 1000, step)]
            breath_amps.extend([ii for ii in range(10, -1, -step)])
            for ii in breath_amps:
                for led in self.spheres:
                    self.__set(led, color)
                for led in self.paths:
                    self.__set(led, color)
                self.__show(ii/25)  # noqa
            repeat -= 1
        self.clear()

    def breathing_led(self, led, color=RED, repeat=1):
        """
        Method to handle a breathing led animation

        Params:
            led: int
            color: tuple, optional
            repeat: int, optional
        """
        while repeat > 0:
            self.clear()
            step = 5
            breath_amps = [ii for ii in range(0, 1000, step)]
            breath_amps.extend([ii for ii in range(1000, -1, -step)])
            for ii in breath_amps:
                self.__set(led, color)
                self.__show(ii / 255)  # noqa
                sleep(0.02)
            repeat -= 1

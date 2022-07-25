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

# UNITTEST
# --------
# import unittest
# unittest.main('test_nrf24l01')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import utime
import unittest

from machine import Pin, SPI


class TestNRF24l01(unittest.TestCase):
    """
    Test class to test nrf24l01 module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        nrf_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
                      mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
        from nrf24l01 import NRF  # noqa
        self.nrf = NRF(nrf_spi, csn=Pin(3, Pin.OUT), ce=Pin(0, Pin.OUT))

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test___config(self):
        """
        test __config functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.nrf.__config()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___read_reg(self):
        """
        test __read_reg functionality
        """
        # Params
        reg = 0x01
        # Returns
        return_1 = b'\x03'
        # Calls
        result = self.nrf.__read_reg(reg)
        # Asserts
        self.assertEqual(result, return_1)

    def test___write_reg(self):
        """
        test __write_reg functionality
        """
        # Params
        reg = 0x01
        value = 0x01
        # Returns
        return_1 = None
        # Calls
        none_1 = self.nrf.__write_reg(reg, value)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___mode_tx(self):
        """
        test __mode_tx functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.nrf.__mode_tx()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___mode_rx(self):
        """
        test __mode_rx functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.nrf.__mode_rx()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___send_msg(self):
        """
        test __send_msg functionality
        """
        # Params
        msg = 'foo'
        # Returns
        return_1 = None
        # Calls
        self.nrf.__mode_tx()
        none_1 = self.nrf.__send_msg(msg)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___new_msg(self):
        """
        test __new_msg functionality
        """
        # Params
        msg = 'foo'
        # Returns
        return_1 = False
        # Calls
        self.nrf.__mode_tx()
        self.nrf.__send_msg(msg)
        utime.sleep(0.001)
        self.nrf.__mode_rx()
        has_new_message = self.nrf.__new_msg()
        utime.sleep(0.001)
        # Asserts
        self.assertEqual(has_new_message, return_1)

    def test___read_msg(self):
        """
        test __read_msg functionality
        """
        # Returns
        return_1 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'  # noqa
        # Calls
        self.nrf.__mode_tx()
        msg = self.nrf.__read_msg()
        # Asserts
        self.assertEqual(msg, return_1)

    def test_recv(self):
        """
        test recv functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.nrf.recv()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_send(self):
        """
        test send functionality
        """
        # Params
        msg = 'foo'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.nrf.send(msg)
        # Asserts
        self.assertEqual(none_1, return_1)

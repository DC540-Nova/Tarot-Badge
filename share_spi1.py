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

from machine import Pin


class Device:
    """
    Class to handle sharing spi1 on two devices
    """

    def __init__(self):
        self.sd_card_cs = Pin(9)
        self.sd_card_cs.value(1)  # drive sd card cs high on init
        self.nrf_cs = Pin(1)
        self.nrf_cs.value(1)  # drive nrf cs high on init

    def activate_sd_card(self):
        """
        Method to activate sd card for usage
        """
        self.sd_card_cs.value(0)  # drive sd cs card low so that it is ready to use

    def deactivate_sd_card(self):
        """
        Method to deactivate sd card for when not in use
        """
        self.sd_card_cs.value(1)  # drive sd cs card high when not in use so other device can access

    def activate_nrf(self):
        """
        Method to activate nrf for usage
        """
        self.nrf_cs.value(0)  # drive nrf cs low so that it is ready to use

    def deactivate_nrf(self):
        """
        Method to deactivate nrf for when not in use
        """
        self.nrf_cs.value(1)  # drive nrf high when not in use so other device can access

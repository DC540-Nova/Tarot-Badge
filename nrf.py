# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
# Developer: Corinne "Rinn" Neidig
#
# Copyright (c) 2021 DC540 Defcon Group
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

from utime import sleep, sleep_ms, sleep_us, ticks_ms, ticks_diff
import ustruct as struct
from micropython import const

import microcontroller
import file_manager
from neo_pixel import NeoPixel
from config import *

neo_pixel = NeoPixel(Pin)

# nRF24L01+ registers
CONFIG = const(0x00)
EN_RXADDR = const(0x02)
SETUP_AW = const(0x03)
SETUP_RETR = const(0x04)
RF_CH = const(0x05)
RF_SETUP = const(0x06)
STATUS = const(0x07)
RX_ADDR_P0 = const(0x0A)
TX_ADDR = const(0x10)
RX_PW_P0 = const(0x11)
FIFO_STATUS = const(0x17)
DYNPD = const(0x1C)
EN_CRC = const(0x08)
CRCO = const(0x04)
PWR_UP = const(0x02)
PRIM_RX = const(0x01)
POWER_0 = const(0x00)
POWER_1 = const(0x02)
POWER_2 = const(0x04)
POWER_3 = const(0x06)
SPEED_1M = const(0x00)
SPEED_2M = const(0x08)
SPEED_250K = const(0x20)
RX_DR = const(0x40)
TX_DS = const(0x20)
MAX_RT = const(0x10)
RX_EMPTY = const(0x01)
R_RX_PL_WID = const(0x60)
R_RX_PAYLOAD = const(0x61)
W_TX_PAYLOAD = const(0xA0)
FLUSH_TX = const(0xE1)
FLUSH_RX = const(0xE2)
NOP = const(0xFF)


class NRF24L01:
    """
    Class to handle the NRF driver
    """

    def __init__(self, spi, cs, ce, channel=46, payload_size=16):  # noqa
        """
        Params:
            spi: object
            cs: int
            ce: int
            channel: int, optional
            payload_size: int, optional
        """
        assert payload_size <= 32
        self.buf = bytearray(1)
        # store the pins
        self.spi = spi
        self.cs = cs
        self.ce = ce
        # init the SPI bus and pins
        self.init_spi(4000000)
        # reset everything
        ce.init(ce.OUT, value=0)
        cs.init(cs.OUT, value=1)
        self.payload_size = payload_size
        self.pipe0_read_addr = None
        sleep_ms(5)
        # set address width to 5 bytes and check for device present
        self.reg_write(SETUP_AW, 0b11)
        sleep_ms(5)
        if self.reg_read(SETUP_AW) != 0b11:
            raise OSError('nRF24L01+ Hardware not responding')
        # disable dynamic payloads
        self.reg_write(DYNPD, 0)
        # auto retransmit delay: 1750us
        # auto retransmit count: 8
        self.reg_write(SETUP_RETR, (6 << 4) | 8)
        # set rf power and speed
        self.set_power_speed(POWER_3, SPEED_250K)  # Best for point to point links
        # init CRC
        self.set_crc(2)
        # clear status flags
        self.reg_write(STATUS, RX_DR | TX_DS | MAX_RT)
        # set channel
        self.set_channel(channel)
        # flush buffers
        self.flush_rx()
        self.flush_tx()

    def init_spi(self, baudrate):
        """
        Method to handle SPI init

        Params:
            baudrate: int
        """
        try:
            master = self.spi.MASTER
        except AttributeError:
            self.spi.init(baudrate=baudrate, polarity=0, phase=0)
        else:
            self.spi.init(master, baudrate=baudrate, polarity=0, phase=0)

    def reg_read(self, reg):
        """
        Method to handle register read

        Params:
            reg: int

        Returns:
            int
        """
        self.cs(0)
        self.spi.readinto(self.buf, reg)
        self.spi.readinto(self.buf)
        self.cs(1)
        return self.buf[0]

    def reg_write_bytes(self, reg, buf):
        """
        Method to handle register write bytes

        Params:
            reg: int
            buf: int

        Returns:
            int
        """
        self.cs(0)
        self.spi.readinto(self.buf, 0x20 | reg)
        self.spi.write(buf)
        self.cs(1)
        return self.buf[0]

    def reg_write(self, reg, value):
        """
        Method to handle register write

        Params:
            reg: int
            value: int

        Returns:
            int
        """
        self.cs(0)
        self.spi.readinto(self.buf, 0x20 | reg)
        ret = self.buf[0]
        self.spi.readinto(self.buf, value)
        self.cs(1)
        return ret

    def flush_rx(self):
        """
        Method to handle flush rx
        """
        self.cs(0)
        self.spi.readinto(self.buf, FLUSH_RX)
        self.cs(1)

    def flush_tx(self):
        """
        Class to handle flush tx
        """
        self.cs(0)
        self.spi.readinto(self.buf, FLUSH_TX)
        self.cs(1)

    def set_power_speed(self, power, speed):
        """
        Method to handle setting the power speed

        Params:
            power: int
            speed: int
        """
        setup = self.reg_read(RF_SETUP) & 0b11010001
        self.reg_write(RF_SETUP, setup | power | speed)

    def set_crc(self, length):
        """
        Method to handle setting the crc

        Params:
            length: int
        """
        config = self.reg_read(CONFIG) & ~(CRCO | EN_CRC)
        if length == 0:
            pass
        elif length == 1:
            config |= EN_CRC
        else:
            config |= EN_CRC | CRCO
        self.reg_write(CONFIG, config)

    def set_channel(self, channel):
        """
        Method to handle setting the channel

        Params:
            channel: int
        """
        self.reg_write(RF_CH, min(channel, 125))

    def open_tx_pipe(self, address):
        """
        Method to handle opening the tx pipe

        Params:
            addreses: int
        """
        assert len(address) == 5
        self.reg_write_bytes(RX_ADDR_P0, address)
        self.reg_write_bytes(TX_ADDR, address)
        self.reg_write(RX_PW_P0, self.payload_size)

    def open_rx_pipe(self, pipe_id, address):
        """
        Method to handle opening the rx pipe

        Params:
            pipe_id: int
            addreses: int
        """
        assert len(address) == 5
        assert 0 <= pipe_id <= 5
        if pipe_id == 0:
            self.pipe0_read_addr = address
        if pipe_id < 2:
            self.reg_write_bytes(RX_ADDR_P0 + pipe_id, address)
        else:
            self.reg_write(RX_ADDR_P0 + pipe_id, address[0])
        self.reg_write(RX_PW_P0 + pipe_id, self.payload_size)
        self.reg_write(EN_RXADDR, self.reg_read(EN_RXADDR) | (1 << pipe_id))

    def start_listening(self):
        """
        Method to handle start listening
        """
        self.reg_write(CONFIG, self.reg_read(CONFIG) | PWR_UP | PRIM_RX)
        self.reg_write(STATUS, RX_DR | TX_DS | MAX_RT)
        if self.pipe0_read_addr is not None:
            self.reg_write_bytes(RX_ADDR_P0, self.pipe0_read_addr)
        self.flush_rx()
        self.flush_tx()
        self.ce(1)
        sleep_us(130)

    def stop_listening(self):
        """
        Method to handle stop listening
        """
        self.ce(0)
        self.flush_tx()
        self.flush_rx()

    def any(self):
        """
        Method to handle reporting status

        Returns:
            bool
        """
        return not bool(self.reg_read(FIFO_STATUS) & RX_EMPTY)

    def recv(self):
        """
        Method to handle recv

        Returns:
            int
        """
        # get the data
        self.cs(0)
        self.spi.readinto(self.buf, R_RX_PAYLOAD)
        buf = self.spi.read(self.payload_size)
        self.cs(1)
        # clear RX ready flag
        self.reg_write(STATUS, RX_DR)
        return buf

    def send(self, buf, timeout=500):
        """
        Method to handle send

        Params:
            buf: int
            timeout: int, optional
        """
        self.send_start(buf)
        start = ticks_ms()
        result = None
        while result is None and ticks_diff(ticks_ms(), start) < timeout:
            result = self.send_done()  # 1 == success, 2 == fail
        if result == 2:
            raise OSError('send failed')

    def send_start(self, buf):
        """
        Method to handle opening send start

        Params:
            buf: int
        """
        # power up
        self.reg_write(CONFIG, (self.reg_read(CONFIG) | PWR_UP) & ~PRIM_RX)
        sleep_us(150)
        # send the data
        self.cs(0)
        self.spi.readinto(self.buf, W_TX_PAYLOAD)
        self.spi.write(buf)
        if len(buf) < self.payload_size:
            self.spi.write(b"\x00" * (self.payload_size - len(buf)))  # pad out data
        self.cs(1)
        # enable the chip so it can send the data
        self.ce(1)
        sleep_us(15)  # needs to be > 10us
        self.ce(0)

    def send_done(self):
        """
        Method to handle send done

        Returns:
            None, int
        """
        if not (self.reg_read(STATUS) & (TX_DS | MAX_RT)):
            return None  # tx not finished
        # either finished or failed: get and clear status flags, power down
        status = self.reg_write(STATUS, RX_DR | TX_DS | MAX_RT)
        self.reg_write(CONFIG, self.reg_read(CONFIG) & ~PWR_UP)
        return 1 if status & TX_DS else 2


class NRF:
    """
    Class to handle the NRF functionality
    """

    def __init__(self):
        csn = Pin(cfg['csn'], mode=Pin.OUT, value=1)
        ce = Pin(cfg['ce'], mode=Pin.OUT, value=0)
        if cfg['spi'] == -1:
            spi = SPI(-1, sck=Pin(cfg['sck']), cipo=Pin(cfg['cipo']), copi=Pin(cfg['copi']))   # noqa
            self.nrf = NRF24L01(spi, csn, ce, payload_size=8)  # noqa
        else:
            self.nrf = NRF24L01(SPI(cfg['spi']), csn, ce, payload_size=8)

    def send(self, message, message_sent=False):
        """
        Method to send nrf data

        Params:
            message: str
            sending_message: bool, optional
        """
        self.nrf.open_tx_pipe(PIPES[0])
        self.nrf.open_rx_pipe(1, PIPES[1])
        self.nrf.start_listening()
        num_needed = 1
        num_successes = 0
        num_failures = 0
        led_state = 0
        while num_successes < num_needed and num_failures < num_needed:
            # stop listening and send packet
            self.nrf.stop_listening()
            led_state = max(1, (led_state << 1) & 0x0F)
            try:
                for letter in message:
                    letter = ord(letter)
                    self.nrf.send(struct.pack('ii', letter, led_state))
            except OSError:
                pass
            # start listening again
            self.nrf.start_listening()
            # wait for response, with 250ms timeout
            start_time = ticks_ms()
            timeout = False
            while not self.nrf.any() and not timeout:
                if ticks_diff(ticks_ms(), start_time) > 250:
                    timeout = True
            if timeout:
                num_failures += 1
            else:
                num_successes += 1
            # delay then loop
            sleep_ms(250)
            if message_sent and message:
                message = 'Message Sent!'
                display.scroll_text([[0, 0, message]], len(message))
                sleep(1)

    def recv(self, interval=80000, display_word=True, sleep_time=15, badge_id=False):
        """
        Method to send recv data

        Params:
            interval: int, optional
            display_word: bool, optional
            sleep_time: int, optional
            badge_id: bool, optional

        Returns:
            str or None
        """
        _RX_POLL_DELAY = const(15)
        _RECV_SEND_DELAY = const(10)
        self.nrf.open_tx_pipe(PIPES[0])
        self.nrf.open_rx_pipe(1, PIPES[1])
        self.nrf.start_listening()
        time = 0
        word = []
        # 24000 = 3 seconds
        while time < interval:
            time += 1
            if time > interval:
                break
            if self.nrf.any():
                while self.nrf.any():
                    buf = self.nrf.recv()
                    letter, led_state = struct.unpack('ii', buf)
                    letter = chr(letter)
                    word.append(letter)
                    sleep_ms(_RX_POLL_DELAY)
                # give sender time to get into receive mode
                sleep_ms(_RECV_SEND_DELAY)
                # convert to str
                word = ''.join(str(element) for element in word)
                if display_word:
                    if badge_id:
                        # there is an edge case where some NRF modules are appending the last char of their own
                        # unique_id to the beginning of the foreign_unique_id string
                        if len(word) == 17:
                            word = word[1:]
                    display.scroll_text([[0, 0, word]], len(word))
                    sleep(sleep_time)
                self.nrf.stop_listening()
                try:
                    letter = ord(letter)  # noqa
                    self.nrf.send(struct.pack('i', letter))
                except OSError:
                    pass
                self.nrf.start_listening()
                return word

    def boss_send_id(self):
        """
        Method to check for a boss id and if they are a boss, send id
        """
        my_id_hex = microcontroller.get_unique_id()
        for id in boss_ids:  # noqa
            if my_id_hex == id:
                self.send(my_id_hex)
                break

    def check_for_boss(self):
        """
        Method to check for a boss badge
        """
        display.text('Scanning...')
        foreign_unique_id = self.recv(interval=104000, display_word=False)
        foreign_unique_id = str(foreign_unique_id)
        # there is an edge case where some NRF modules are appending the last char of their own
        # unique_id to the beginning of the foreign_unique_id string
        if len(foreign_unique_id) == 17:
            foreign_unique_id = foreign_unique_id[1:]
        boss_names_index = 0
        for id in boss_ids:  # noqa
            if foreign_unique_id == id:
                display.scroll_text([[0, 0, boss_names[boss_names_index]]], len(boss_names[boss_names_index]))
                neo_pixel.morse_code(sos, clear_display=False, encrypted=False)
                break
            boss_names_index += 1

    def pair(self, interval=7500):
        """
        Method to pair badges

        Params:
            interval: int, optional
        """
        foreign_unique_id = None  # noqa
        display.text(text='Pairing...')
        unique_id = microcontroller.get_unique_id()
        self.send(unique_id)
        foreign_unique_id = self.recv(interval, badge_id=True)
        self.send(unique_id)
        # try again 8 times to ensure the pairing is successful
        for _ in range(8):
            if not foreign_unique_id:
                foreign_unique_id = self.recv(interval, badge_id=True)
            self.send(unique_id)
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
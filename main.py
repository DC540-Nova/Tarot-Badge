# pip install adafruit-ampy
# ampy -p com5 put main.py
# open micropython terminal - tools - mp - mp REPL
# ctrl-d to load

import utime
from machine import Pin, SPI

import config
import neo_pixel
import sdcard
import uos
from ili9341 import Display, color565
from xglcd_font import XglcdFont
import _thread
import random

neo_pixel = neo_pixel.NeoPixel(Pin)


# config
spi = SPI(
    0,
    baudrate=40000000,
    sck=Pin(6),
    mosi=Pin(7))
display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14))
p0 = Pin(0, Pin.OUT)
p0.value(0)
sd_cs = Pin(9, Pin.OUT)
sd_spi = SPI(
    1,
    baudrate=1000000,
    polarity=0,
    phase=0,
    bits=8,
    firstbit=SPI.MSB,
    sck=Pin(10),
    mosi=Pin(11),
    miso=Pin(8)
)

# initialize SD card
sd = sdcard.SDCard(sd_spi, sd_cs)

# mount sd filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

hex1 = [32, 31, 30, 27, 28, 29, 32]
paths = [28, 30, 29, 26, 22, 21, 23, 24, 19, 14, 13, 16, 17, 12, 11, 10, 8, 6, 3, 5, 2, 1]


def bg_task():
    for _ in range(20):
        for my_LED in hex1:
            neo_pixel.led_on(paths[my_LED - 11], config.COLORS[random.randint(1, 7)])
    utime.sleep_ms(10)
    neo_pixel.led_clear()
    _thread.exit()  # noqa


def sd_test():
    """
    Function to test sd card functionality
    """
    with open('/sd/test01.txt', 'w') as file:
        file.write('Hello, Baab!\r\n')
        file.write('This is the United States calling are we reaching?\r\n')
    with open('/sd/test01.txt', 'r') as file:
        data = file.read()
        print(data)


def img_test():
    """
    Function to test img display functionality
    """
    display.clear()
    display.draw_image('/sd/02-TheHighPriestess.raw', draw_speed=2600)
    p0.value(1)
    utime.sleep(1)
    p0.value(0)


def main_menu():
    """
    Function to display the main menu
    """
    display.clear()
    display.draw_text(0, 0, 'MAIN MENU', unispace, color565(255, 128, 0))
    display.draw_text(0, 25, 'up: Badge ID', unispace, color565(255, 255, 0))
    display.draw_text(0, 50, 'down: Games', unispace, color565(255, 255, 0))
    display.draw_text(0, 75, 'lt: Phonebooth', unispace, color565(255, 255, 0))
    p0.value(1)


unispace = XglcdFont('Unispace12x24.c', 12, 24)
sd_test()
print("main thread img_test")
_thread.start_new_thread(bg_task, ())  # noqa
img_test()
main_menu()

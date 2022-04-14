from time import sleep
from machine import Pin, SPI
#import machine
import sdcard
import uos
from ili9341 import Display, color565
from time import sleep
from xglcd_font import XglcdFont

# config 
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14))
sd_cs = machine.Pin(9, machine.Pin.OUT)
sd_spi = machine.SPI(1, baudrate=40000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB, sck=machine.Pin(10), mosi=machine.Pin(11), miso=machine.Pin(8))

# initialize SD card
sd = sdcard.SDCard(sd_spi, sd_cs)

# mount sd filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

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
    # display.clear()
    display.draw_image('/sd/02-TheHighPriestess.raw')
    sleep(1)

def font_test():
    """
    Function to test various fonts
    """
    display.clear()
    print('Loading fonts...')
    print('Loading arcadepix')
    arcadepix = XglcdFont('fonts/ArcadePix9x11.c', 9, 11)
    print('Loading bally')
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    print('Loading broadway')
    broadway = XglcdFont('fonts/Broadway17x15.c', 17, 15)
    print('Loading espresso_dolce')
    espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    print('Loading fixed_font')
    fixed_font = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
    print('Loading neato')
    neato = XglcdFont('fonts/Neato5x7.c', 5, 7, letter_count=223)
    print('Loading robotron')
    robotron = XglcdFont('fonts/Robotron13x21.c', 13, 21)
    print('Loading unispace')
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    print('Loading wendy')
    wendy = XglcdFont('fonts/Wendy7x8.c', 7, 8)
    print('Fonts loaded...')
    display.draw_text(0, 0, 'Arcade Pix 9x11', arcadepix, color565(255, 0, 0))
    display.draw_text(0, 22, 'Bally 7x9', bally, color565(0, 255, 0))
    display.draw_text(0, 43, 'Broadway 17x15', broadway, color565(0, 0, 255))
    display.draw_text(0, 66, 'Espresso Dolce 18x24', espresso_dolce, color565(0, 255, 255))
    display.draw_text(0, 104, 'Fixed Font 5x8', fixed_font, color565(255, 0, 255))
    display.draw_text(0, 125, 'Neato 5x7', neato, color565(255, 255, 0))
    display.draw_text(0, 155, 'ROBOTRON 13X21', robotron, color565(255, 255, 255))
    display.draw_text(0, 190, 'Unispace 12x24', unispace, color565(255, 128, 0))
    display.draw_text(0, 220, 'Wendy 7x8', wendy, color565(255, 0, 128))
    sleep(5)
    
def main_menu():
    """
    Function to display the main menu
    """
    #display.clear()
    display.draw_text(0, 0, 'MAIN MENU', unispace, color565(255, 128, 0))
    display.draw_text(0, 25, 'up: Badge ID', unispace, color565(255, 255, 0))
    display.draw_text(0, 50, 'down: Games', unispace, color565(255, 255, 0))
    display.draw_text(0, 75, 'lt: Phonebooth', unispace, color565(255, 255, 0))

 
    #text('rt: Extras', x=0, y=47, start_clear=False)
    #text('submit: Reset', x=0, y=57, start_clear=False)

#bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
#sd_test()
img_test()
main_menu()
#font_test()


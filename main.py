from time import sleep
from machine import Pin, SPI
import machine
import sdcard
import uos
from ili9341 import Display, color565
from time import sleep
from xglcd_font import XglcdFont

# Baud rate of 40000000 seems about the max
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14))

# Assign chip select (CS) pin (and start it high)
sd_cs = machine.Pin(9, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
sd_spi = machine.SPI(1,
                  baudrate=40000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(8))

# Initialize SD card
sd = sdcard.SDCard(sd_spi, sd_cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

def sd_test():
    # Create a file and write something to it
    with open("/sd/test01.txt", "w") as file:
        file.write("Hello, Baab!\r\n")
        file.write("This is the United States calling are we reaching?\r\n")

    # Open the file we just created and read from it
    with open("/sd/test01.txt", "r") as file:
        data = file.read()
        print(data)

def test():
    #display.clear()
    #display.draw_image('/sd/00-TheFool.raw', 0, 0, 240, 320)
    #sleep(1)
    
    #display.draw_image('/sd/01-TheMagician.raw', 0, 0, 240, 320)
    #sleep(5)
    
    display.draw_image('/sd/02-TheHighPriestess.raw')
    sleep(1)

    #display.cleanup()

def text():
    #print('Loading fonts...')
    #print('Loading arcadepix')
    display.clear()
    #arcadepix = XglcdFont('fonts/ArcadePix9x11.c', 9, 11)
    #print('Loading bally')
    #bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    #print('Loading broadway')
    #broadway = XglcdFont('fonts/Broadway17x15.c', 17, 15)
    #print('Loading espresso_dolce')
    espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    #print('Loading fixed_font')
    #fixed_font = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
    #print('Loading neato')
    #neato = XglcdFont('fonts/Neato5x7.c', 5, 7, letter_count=223)
    #print('Loading robotron')
    #robotron = XglcdFont('fonts/Robotron13x21.c', 13, 21)
    #print('Loading unispace')
    #unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    #print('Loading wendy')
    #wendy = XglcdFont('fonts/Wendy7x8.c', 7, 8)
    #print('Fonts loaded.')

    #display.draw_text(0, 0, 'Arcade Pix 9x11', arcadepix, color565(255, 0, 0))
    #display.draw_text(0, 22, 'Bally 7x9', bally, color565(0, 255, 0))
    #display.draw_text(0, 43, 'Broadway 17x15', broadway, color565(0, 0, 255))
    display.draw_text(15, 10, 'Scrolling Baab', espresso_dolce,
                      color565(255, 255, 0))
    display.draw_text(15, 40, 'Scrolling Baab', espresso_dolce,
                      color565(255, 255, 0))
    #display.draw_text(15, 40, 'The Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginner\'s luck, improvisation and believing in the universe.', espresso_dolce,
    #                  color565(255, 0, 0))
    display.set_scroll(top=20, bottom=10)
    #spectrum = list(range(152, 221)) + list(reversed(range(152, 220)))

    for y in reversed(range(200)):
        display.scroll(y)
        sleep(.05)


    #display.draw_text(0, 104, 'Fixed Font 5x8', fixed_font,
    #                  color565(255, 0, 255))
    #display.draw_text(0, 125, 'Neato 5x7', neato, color565(255, 255, 0))
    #display.draw_text(0, 155, 'ROBOTRON 13X21', robotron,
    #                  color565(255, 255, 255))
    #display.draw_text(0, 190, 'Unispace 12x24', unispace,
    #                  color565(255, 128, 0))
    #display.draw_text(0, 220, 'Wendy 7x8', wendy, color565(255, 0, 128))

    sleep(1)
    display.clear()


test()
#text()
#sd_test()


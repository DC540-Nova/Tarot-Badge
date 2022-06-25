#!/bin/sh

source venv/bin/activate
mpremote connect /dev/tty.u* cp boot.py :
mpremote connect /dev/tty.u* cp Unispace12x24.c :
mpremote connect /dev/tty.u* cp config.py :
mpremote connect /dev/tty.u* cp ili9341.py :
mpremote connect /dev/tty.u* cp main.py :
mpremote connect /dev/tty.u* cp neo_pixel.py :
mpremote connect /dev/tty.u* cp sd_card.py :
mpremote connect /dev/tty.u* cp file_manager.py :
mpremote connect /dev/tty.u* cp microcontroller.py :
mpremote connect /dev/tty.u* cp game.py :
mpremote connect /dev/tty.u* cp button.py :
mpremote connect /dev/tty.u* cp data.py :
mpremote connect /dev/tty.u* cp menu.py :
mpremote connect /dev/tty.u* cp tarot.py :
mpremote connect /dev/tty.u* cp pair.py :
mpremote connect /dev/tty.u* cp unittest.py :
mpremote connect /dev/tty.u* cp morse_code.py :
mpremote connect /dev/tty.u* cp encryption.py :

#!/bin/sh

cp main.c pico/micropython/ports/rp2
cp obj.c pico/micropython/py
cp data.py pico/micropython/ports/rp2/modules
cp demo.py pico/micropython/ports/rp2/modules
cp encryption.py pico/micropython/ports/rp2/modules
cp file_manager.py pico/micropython/ports/rp2/modules
cp game.py pico/micropython/ports/rp2/modules
cp ili9341.py pico/micropython/ports/rp2/modules
cp main.py pico/micropython/ports/rp2/modules
cp menu.py pico/micropython/ports/rp2/modules
cp microcontroller.py pico/micropython/ports/rp2/modules
cp morse_code.py pico/micropython/ports/rp2/modules
cp neo_pixel.py pico/micropython/ports/rp2/modules
cp nrf24l01.py pico/micropython/ports/rp2/modules
cp pair.py pico/micropython/ports/rp2/modules
cp sd_card.py pico/micropython/ports/rp2/modules
cp tarot.py pico/micropython/ports/rp2/modules
cp touch.py pico/micropython/ports/rp2/modules
cd pico/micropython/ports/rp2 && make clean
make
mv build-PICO/firmware.uf2 build-PICO/tb_0.1.0.uf2
cp build-PICO/tb_0.1.0.uf2 ../../../../
cp build-PICO/tb_0.1.0.uf2 /Volumes/RPI-RP2 > /dev/null 2>&1
cd ../../../../

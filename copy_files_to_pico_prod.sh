#!/bin/sh

source venv/bin/activate
mpremote connect /dev/tty.u* cp boot.py :
mpremote connect /dev/tty.u* cp Unispace12x24.c :
mpremote connect /dev/tty.u* cp dc540_logo.raw :
mpremote connect /dev/tty.u* cp 3Hats.raw :

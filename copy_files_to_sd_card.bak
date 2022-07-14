#!/bin/sh

source venv/bin/activate
if [[ $2 == 1 || $2 == 2 || $2 == 3 || $2 == 4 ]]
then
    mpremote connect /dev/tty.u* mkdir /sd/$2 >/dev/null
    mpremote connect /dev/tty.u* cp $1*.* :/sd/$2/
else
    echo "  usage: ./copy_files_to_sd_card.sh <directory> <1, 2, 3 or 4>"
fi

#!/bin/sh

source venv/bin/activate
if [[ ($2 =~ [^A-Za-z0-9]) || (-z $2) || ! (-z $3) || (${#2} -gt 8) ]]
then
  echo "  usage: ./copy_files_to_sd_card.sh <directory> <card_deck>"
else
    echo "That URL is allowed."
fi
#    mpremote connect /dev/tty.u* mkdir /sd/$2 >/dev/null
#    mpremote connect /dev/tty.u* cp $1*.* :/sd/$2/

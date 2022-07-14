#!/bin/sh

source venv/bin/activate
if [[ ($2 =~ [^A-Za-z0-9\-]) || (-z $2) || ! (-z $3) || (${#2} -gt 11) ]]
then
  echo "  usage: ./copy_files_to_sd_card.sh <directory> <card_deck>"
  echo "         DECK MUST BE LESS THAN OR EQUAL TO 12 CHARS AND NO SPACES"
else
    mpremote connect /dev/tty.u* mkdir /sd/"$2" >/dev/null
    mpremote connect /dev/tty.u* cp "$1"*.* :/sd/"$2"/
fi

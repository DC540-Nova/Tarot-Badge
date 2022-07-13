#!/bin/sh

source venv/bin/activate
mpremote connect /dev/tty.u* cp $1*.* :/sd/$2

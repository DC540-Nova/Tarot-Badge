#!/bin/sh

source venv/bin/activate
python convert.py
python convert_to_raw.py

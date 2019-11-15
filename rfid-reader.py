#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Avvicina il tag rfid")

try:
    id, timestamps = reader.read()
    print(id)
    print(text)

finally:
    GPIO.cleanup()
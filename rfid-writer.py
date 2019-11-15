#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime

reader = SimpleMFRC522()

try:
        # id dell'attrezzo gia inserito nel database mysql
        idAttrezzo = input('Inserisci id dell attrezzo: ')
        # timestamp attuale
        timestamps = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Avvicina il tag all lettore")
        data = '%d; %s' %(idAttrezzo, timestamps)
        reader.write(data)
        print("Informazioni salvate")
finally:
        GPIO.cleanup()
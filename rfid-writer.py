#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime

reader = SimpleMFRC522()

try:
        #====================================================================
        # ID ATTREZZO E' RELATIVO A QUELLO SALVATO NEL DATABASE 
        #====================================================================
        idAttrezzo = input('Inserisci id dell attrezzo: ')
        # timestamp attuale
        #timestamps = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Avvicina il tag all lettore")
        #data = '%d; %s' %(idAttrezzo, timestamps)
        data = idAttrezzo
        reader.write(data)
        print("Informazioni salvate")
finally:
        GPIO.cleanup()
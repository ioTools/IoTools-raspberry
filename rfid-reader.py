#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import gps
import requests

#=========================================
# CONTIENE L'ID DEL FURGONE (GIA INSERITO NEL DB)
try
    fh=open("idFurgone.txt","r")
    idFurgone = fh.read()
except
    idFurgone= None
#=========================================


reader = SimpleMFRC522()

print("Avvicina il tag rfid")

try:
    # legge ID e Timestamps dal tag
    data = reader.read()
    #data.split("_")
    idAttrezzo = data
    #time= data[1]
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # avvia una sessione per il gps
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    while True :
        rep = session.next()
        try :
            if (rep["class"] == "TPV") :
             		print(str(rep.lat) + "," + str(rep.lon))
                    lat = str(rep.lat)
                    long = str(rep.lon)
                    GETdata = {"idFurgone": idFurgone, "idAttrezzo": idAttrezzo, "timestamp": time, "lat": lat, "long": long}
                    r = requests.get("http://www.iotools.altervista.com/api/getRfidData.php", params=GETdata)
                    # http://www.iotools.altervista.com/api/getRfidData.php?idFurgone=1&ecc...                   
                    print(r.url)
                    break
        except Exception as e :
            print("Got exception " + str(e))

finally:
    GPIO.cleanup()
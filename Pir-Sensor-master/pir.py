#!/usr/bin/env python
 
import serial
import sys
import time
import RPi.GPIO as io
import subprocess
import mysql.connector
<<<<<<< HEAD
import webbrowser
from datetime import datetime
=======

>>>>>>> 6951405603dcf9b885a3db08ebbc5c09bf0b9a06
mydb = mysql.connector.connect(
    host="databasepeili.c1emz48wiw83.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="alypeili",
    database="innodb",
)
mycursor= mydb.cursor()

<<<<<<< HEAD
sql = "INSERT INTO weather (temperature, datetime) VALUES (%s, %s)"
=======
sql = "INSERT INTO WEATHER (wtemperature) VALUES (%s)"
>>>>>>> 6951405603dcf9b885a3db08ebbc5c09bf0b9a06
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 10  # seconds
PIR_PIN = 17        # Pin 11 on the board
<<<<<<< HEAD
port = serial.Serial("/dev/ttyACM0", baudrate=9600)
=======
port = serial.Serial("/dev/ttyAMA0", baudrate=9600)
>>>>>>> 6951405603dcf9b885a3db08ebbc5c09bf0b9a06

def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
<<<<<<< HEAD
     
    while True:
        
        
        
        rcv = port.readline()
        
        dtime = datetime.now()       
        val = (rcv, dtime)
        mycursor.execute(sql, val)
        mydb.commit()
        print(rcv)
        
            
=======
 
    while True:
        rcv = port.readline()
        #mycursor.execute(sql, rcv)
        #mydb.commit()
        print(rcv)

>>>>>>> 6951405603dcf9b885a3db08ebbc5c09bf0b9a06
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
<<<<<<< HEAD
                webbrowser.open_new('/home/pi/Documents/tiimiRepo/Pir-Sensor-master/ui.html')
=======
>>>>>>> 6951405603dcf9b885a3db08ebbc5c09bf0b9a06
        else:
            if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
        time.sleep(.1)
 
def turn_on():
    subprocess.call("sh monitor_on.sh", shell=True)
 
def turn_off():
    subprocess.call("sh monitor_off.sh", shell=True)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()

#!/usr/bin/env python
 
import serial
import sys
import time
import RPi.GPIO as io
import subprocess
import mysql.connector

mydb = mysql.connector.connect(
    host="databasepeili.c1emz48wiw83.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="alypeili",
    database="innodb",
)
mycursor= mydb.cursor()

sql = "INSERT INTO WEATHER (wtemperature) VALUES (%s)"
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 10  # seconds
PIR_PIN = 17        # Pin 11 on the board
port = serial.Serial("/dev/ttyAMA0", baudrate=9600)

def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
 
    while True:
        rcv = port.readline()
        #mycursor.execute(sql, rcv)
        #mydb.commit()
        print(rcv)

        if io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
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

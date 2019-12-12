#!/usr/bin/env python
 
import serial
import sys
import time
import RPi.GPIO as io
import subprocess
import mysql.connector
import webbrowser
from datetime import datetime


    
sql = "INSERT INTO weather (temperature, datetime) VALUES (%s, %s)"
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 15  # seconds
PIR_PIN = 17        # Pin 11 on the board
port = serial.Serial("/dev/ttyACM0", baudrate=9600)

def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
    #turn_off()
#     webbrowser.open_new('http://ec2-3-85-231-250.compute-1.amazonaws.com/')
    time.sleep(10)
    try:
        mydb = mysql.connector.connect(
            host="databasepeili.c1emz48wiw83.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="alypeili",
            database="innodb",
        )
        mycursor= mydb.cursor()
        
    except mysql.connector.Error as err:
        print("something went wrong: {}".format(err))
    
    while True:
        
        
        
        rcv = port.readline()
        
        dtime = datetime.now()       
        val = (rcv, dtime)
        mycursor.execute(sql, val)
        mydb.commit()
	time.sleep(1)
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

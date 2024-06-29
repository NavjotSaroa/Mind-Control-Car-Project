"""
Author: Navjot Saroa

This file will take the same recording system, but now send it off to the Arduino to trigger events, eventually running a car when 
I get that 3D printed.
"""

from SoundTest import makeKNN, collectaudio
import pickle
import os
import serial
import time

if not os.path.exists("musicdata_1.pkl"):
    makeKNN(1)

with open("musicdata_1.pkl", "rb") as file:
    knn = pickle.load(file)

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1) 


def write_read(x): 
    arduino.write(bytes(x, 'utf-8')) 
    time.sleep(0.05) 
    data = arduino.readline() 
    return data 


while True: 
    input("Press enter to start ")
    data = collectaudio()[1][10:71]
    pre = knn.predict([data])
    if pre == 97:
        write_read("0")
    elif pre == 98:
        write_read("1")
    elif pre == 99:
        write_read("2")
    elif pre <= 103:
        write_read("3")

    time.sleep(1)


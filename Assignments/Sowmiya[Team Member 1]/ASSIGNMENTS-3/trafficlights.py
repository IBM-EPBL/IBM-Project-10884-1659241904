#!/usr/bin/python3.4
import RPi.GPIO as GPIO  
import time     

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  # Button
GPIO.setup(17, GPIO.OUT, initial = GPIO.HIGH)         # RED
GPIO.setup(27, GPIO.OUT, initial = GPIO.HIGH)         # YELLOW
GPIO.setup(18, GPIO.OUT, initial = GPIO.HIGH)         # GREEN
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)          # Buzzer

x = 1           #  Variable to control traffic light system
try:
while True:
if(GPIO.input(4) == True):
while(x == 1):
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.HIGH)
time.sleep(2)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
time.sleep(3)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
GPIO.output(18, GPIO.LOW)
time.sleep(5)
GPIO.output(18, GPIO.HIGH)
time.sleep(2)
except Exception as ex:
print(“error occured”,ex)
finally:
GPIO.cleanup()

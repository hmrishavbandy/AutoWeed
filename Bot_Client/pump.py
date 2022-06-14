import RPi.GPIO as GPIO
from time import sleep
import time

def run_pump():
    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM) 
    #GPIO.setmode(GPIO.BOARD)

    Motor1 = 23
    Motor2 = 24

    GPIO.setup(Motor1,GPIO.OUT)

    GPIO.output(Motor1,GPIO.LOW)
    time.sleep(2)
    GPIO.output(Motor1,GPIO.HIGH)

import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
import time
GPIO.setmode(GPIO.BCM) 
#GPIO.setmode(GPIO.BOARD)

Motor1 = 2
Motor2 = 4
Motor3 = 14
Motor4 = 15

Motor5 = 17
Motor6 = 27

Motor7=6
Motor8=13
Motor9=19
Motor10=26

Motor11=0
Motor12=5


GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor5,GPIO.OUT)
GPIO.setup(Motor6,GPIO.OUT)
GPIO.setup(Motor7,GPIO.OUT)
GPIO.setup(Motor8,GPIO.OUT)
GPIO.setup(Motor9,GPIO.OUT)
GPIO.setup(Motor10,GPIO.OUT)
GPIO.setup(Motor11,GPIO.OUT)
GPIO.setup(Motor12,GPIO.OUT)


GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.LOW)
GPIO.output(Motor3,GPIO.LOW)
GPIO.output(Motor4,GPIO.LOW)
GPIO.output(Motor5,GPIO.LOW)
GPIO.output(Motor6,GPIO.LOW)
GPIO.output(Motor7,GPIO.LOW)
GPIO.output(Motor8,GPIO.LOW)
GPIO.output(Motor9,GPIO.LOW)
GPIO.output(Motor10,GPIO.LOW)
GPIO.output(Motor11,GPIO.LOW)
GPIO.output(Motor12,GPIO.LOW)
        
def stopper():

        time.sleep(0.4)
        print("Here")
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.LOW)
        GPIO.output(Motor3,GPIO.LOW)
        GPIO.output(Motor4,GPIO.LOW)
        GPIO.output(Motor5,GPIO.LOW)
        GPIO.output(Motor6,GPIO.LOW)
        GPIO.output(Motor7,GPIO.LOW)
        GPIO.output(Motor8,GPIO.LOW)
        GPIO.output(Motor9,GPIO.LOW)
        GPIO.output(Motor10,GPIO.LOW)
        GPIO.output(Motor11,GPIO.LOW)
        GPIO.output(Motor12,GPIO.LOW)
        #time.sleep(0.1)
ck=1
while ck==1:

    val=input("enter value")
    ch = val

    if ch == 's':                 # Press the key '1'
        
        print("FORWARD MOTION")
        
        GPIO.output(Motor1,GPIO.HIGH)
        GPIO.output(Motor2,GPIO.LOW)
        
        GPIO.output(Motor3,GPIO.LOW)
        GPIO.output(Motor4,GPIO.HIGH)
        
        GPIO.output(Motor7,GPIO.LOW)
        GPIO.output(Motor8,GPIO.HIGH)
        
        GPIO.output(Motor9,GPIO.LOW)
        GPIO.output(Motor10,GPIO.HIGH)
        
        GPIO.output(Motor5,GPIO.HIGH)
        GPIO.output(Motor6,GPIO.HIGH)
        
        GPIO.output(Motor11,GPIO.HIGH)
        GPIO.output(Motor12,GPIO.HIGH)
        stopper()


    elif ch == 'w':                 # Press the key '2'
        print("BACKWARD MOTION")
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.HIGH)
        
        GPIO.output(Motor3,GPIO.HIGH)
        GPIO.output(Motor4,GPIO.LOW)
        
        GPIO.output(Motor7,GPIO.HIGH)
        GPIO.output(Motor8,GPIO.LOW)
        
        GPIO.output(Motor9,GPIO.HIGH)
        GPIO.output(Motor10,GPIO.LOW)
        
        GPIO.output(Motor5,GPIO.HIGH)
        GPIO.output(Motor6,GPIO.HIGH)
        
        GPIO.output(Motor11,GPIO.HIGH)
        GPIO.output(Motor12,GPIO.HIGH)
        stopper()
    
    elif ch == 'a':                 # Press the key '2'
        print("TURN MOTION")
        
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.HIGH)
        
        GPIO.output(Motor3,GPIO.LOW)
        GPIO.output(Motor4,GPIO.HIGH)
        
        GPIO.output(Motor7,GPIO.HIGH)
        GPIO.output(Motor8,GPIO.LOW)
        
        GPIO.output(Motor9,GPIO.LOW)
        GPIO.output(Motor10,GPIO.HIGH)
        
        GPIO.output(Motor5,GPIO.HIGH)
        GPIO.output(Motor6,GPIO.HIGH)
        GPIO.output(Motor11,GPIO.HIGH)
        GPIO.output(Motor12,GPIO.HIGH)
        stopper()
    
    elif ch == 'd':                 # Press the key '2'
        print("TURN MOTION")
        GPIO.output(Motor1,GPIO.HIGH)
        GPIO.output(Motor2,GPIO.LOW)
        
        GPIO.output(Motor3,GPIO.HIGH)
        GPIO.output(Motor4,GPIO.LOW)
        
        GPIO.output(Motor7,GPIO.LOW)
        GPIO.output(Motor8,GPIO.HIGH)
        
        GPIO.output(Motor9,GPIO.HIGH)
        GPIO.output(Motor10,GPIO.LOW)
        
        GPIO.output(Motor5,GPIO.HIGH)
        GPIO.output(Motor6,GPIO.HIGH)
        GPIO.output(Motor11,GPIO.HIGH)
        GPIO.output(Motor12,GPIO.HIGH)
        stopper()
                
        
    elif ch == '5':                  # Press the key '3'
        print("STOP")
        
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.LOW)
        GPIO.output(Motor3,GPIO.LOW)
        GPIO.output(Motor4,GPIO.LOW)
        GPIO.output(Motor5,GPIO.LOW)
        GPIO.output(Motor6,GPIO.LOW)
        GPIO.output(Motor7,GPIO.LOW)
        GPIO.output(Motor8,GPIO.LOW)
        GPIO.output(Motor9,GPIO.LOW)
        GPIO.output(Motor10,GPIO.LOW)
        GPIO.output(Motor11,GPIO.LOW)
        GPIO.output(Motor12,GPIO.LOW)
        
        
    elif ch == '6':                  # Press the key '4'
        print("FINISHED")
        ck=4
        GPIO.cleanup()
    else:
        GPIO.cleanup()
        break

from time import time
from pump import run_pump
import pigpio
import time
pi=pigpio.pi()
servo=20

def spray(bbox,frame):
    bbox_x=(-bbox[0]+bbox[2])/2.0
    #bbox_y=(-bbox[1]+bbox[3])/2.0
    frame_x=frame[0]
    ratio=(bbox_x/frame_x)*5
    pi.set_servo_pulsewidth(servo,1400+ratio*100)
    time.sleep(1)
    #run_pump()

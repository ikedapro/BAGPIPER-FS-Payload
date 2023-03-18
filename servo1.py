# Author: Josh Huang

from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory
import os

factory = PiGPIOFactory()

servo = Servo(24, pin_factory=factory)
servo.value = None

ccw = .115
cw = -.1
t_ratio = .45/90
class Servo1:
    def __init__(self):
        print("servo 1 initiated")
        
        
    def test(self):
        # servo.value = cw
        # time.sleep(0.5)
        # servo.value = ccw
        # time.sleep(0.5)
        servo.value = ccw
        time.sleep(0.45)
        self.stop()
    
    def rotate(self, degrees):
        '''
        Rotates the servo 1 by a number of degrees
        '''
        if degrees > 0: #ccw
            servo.value = ccw
        else:
            servo.value = cw
        time.sleep(t_ratio * abs(degrees))
        self.stop()
       
    def stop(self):
        servo.value = None
        time.sleep(1)


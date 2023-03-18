from gpiozero import Servo
# import math
import time
from gpiozero.pins.pigpio import PiGPIOFactory
# import RPi.GPIO as GPIO
import os

factory = PiGPIOFactory()
# servo = Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo = Servo(23)

class Servo1:
    def __init__(self):
        os.system("sudo pigpiod")
        print("servo 0 initiated")
        
        
    def test(self):
        servo.value = -1
        time.sleep(1)
        self.stop()
    
    def rotate(self, degrees):
        '''
        Rotates the base servo 0 by a number of degrees
        '''
        # servo.value = -40/90
        rot = -degrees + adjustment_angle
        if rot < limit_angle:
            rot = limit_angle
        servo.value = rot/90
        self.stop()
       
    def stop(self):
        time.sleep(0.5)
        servo.value = None

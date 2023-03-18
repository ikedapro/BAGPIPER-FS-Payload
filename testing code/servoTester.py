from gpiozero import Servo
import time
# from gpiozero.pins.pigpio import PiGPIOFactory
#factory = PiGPIOFactory()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
servo1 = GPIO.PWM(24,50)
servo1.start(0)
servo1.ChangeDutyCycle(10)

'''
#servo=Servo(23, pin_factory=factory)
servo=Servo(23)
servo.mid()
time.sleep(5)
servo.min()
time.sleep(3)
servo.max()
time.sleep(3)

'''

from gpiozero import Servo
import time
# from gpiozero.pins.pigpio import PiGPIOFactory
#factory = PiGPIOFactory()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, 1)
time.sleep(5)
GPIO.output(8, 0)
GPIO.cleanup()

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

from picamera import PiCamera
from time import sleep
import os

os.system("libcamera-still -o images/test1.jpg --immediate")
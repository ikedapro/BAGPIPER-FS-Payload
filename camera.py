from picamera import PiCamera
from time import sleep
import os

# camera = PiCamera()
# camera.start_preview()
# sleep(5)
# camera.capture('/images/picture.jpg')
# camera.stop_preview()

os.system("libcamera-still -o images/test1.jpg --immediate")
# use this command to test if camera is installed
# $ vcgencmd get_camera

# use this command to test camera
# $ raspistill -o Desktop/image.jpg
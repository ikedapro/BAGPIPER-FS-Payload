from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/images/picture.jpg')
camera.stop_preview()

# use this command to test if camera is installed
# $ vcgencmd get_camera

# use this command to test camera
# $ raspistill -o Desktop/image.jpg
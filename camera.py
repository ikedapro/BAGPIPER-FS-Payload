import os

class Camera:
    def __init__(self):
        print("camera initiated")
        
    def capture(self, filename):
        os.system(f"libcamera-still -o images/{filename}.jpg --immediate")
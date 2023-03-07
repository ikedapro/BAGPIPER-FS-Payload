# main script that runs upon pi turn on
import time
from imu import IMU

def main():
    # initialize imu
    imu = IMU()
    DC,servo0 = imu.GetAdjustments()
    
    # first set DC, then servos
    # TODO add detection for sudden large changes to imu, which indicates payload has moved, reset and readjust after that
    
    
    print(DC, servo0)

    


if __name__ == "__main__":
    main()
    

 
# main.py
# from MyFile import Square
 
# newClass = Square(5)
# val = newClass.getVal()
 
# print(val)
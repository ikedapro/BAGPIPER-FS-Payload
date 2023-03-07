# main script that runs upon pi turn on
import time
from imu import IMU

def main():
    # initialize imu
    imu = IMU()
    print(imu.debug())
    # while True:
    #     z, x = imu.GetAdjustments()
    #     print(x)
    #     time.sleep(0.5)
    


if __name__ == "__main__":
    main()
    

 
# main.py
# from MyFile import Square
 
# newClass = Square(5)
# val = newClass.getVal()
 
# print(val)
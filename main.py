# main script that runs upon pi turn on
import time
from imu import IMU
from Servo0 import Servo0

def main():
    #region initialize components
    # imu
    imu = IMU()
    # TODO initialize servo 0 class (base)
    # TODO initialize DC motor class
    # TODO initialize radio class
    # TODO initialize servo 1 class (camera)
    #endregion
    
    #region tests
    
    # imu test
    DC,servo_0 = imu.GetAdjustments() #SEE()
    print(DC, servo_0)
    # TODO hardware test servo 0
    # TODO hardware test DC motor
    # TODO hardware test servo 1
    #endregion
    
    # TODO: get servo accelerations and determine if rocket has landed or has moved during payload deployment
    
    #region deployment
    # TODO: use DC class to make adjustments based on imu
    # TODO: use Servo0 class to make adjustments based on imu
    #endregion
    
    #region camera commands
    # TODO use radio class to get a list of commands to execute
    # IDEA: use generator to iterate through commands, see yield and generator in python
    # TODO: use servo 1 class to move camera
    # TODO: use camera class to take pictures and do filters
    #endregion
    
    #???: ability to re-adjust payload if IMU detects payload has shifted?


if __name__ == "__main__":
    main()
# main script that runs upon pi turn on
import time
from imu import IMU
from servo0 import Servo0
from camera import Camera
from radioParser import RadioParser

def main():
    #region initialize components
    # imu
    imu = IMU()
    # TODO initialize servo 0 class (base)
    # TODO initialize DC motor class
    commands = RadioParser()
    # TODO initialize servo 1 class (camera)
    cam = Camera()
    #endregion
    
    #region tests
    
    # imu test
    DC,servo_0 = imu.GetAdjustments()
    print(DC, servo_0)
    # TODO hardware test servo 0
    # TODO hardware test DC motor
    # TODO hardware test servo 1
    cam.capture("class-test")
    #endregion
    
    # TODO: get servo accelerations and determine if rocket has landed or has moved during payload deployment
    
    #region deployment
    # TODO: use DC class to make adjustments based on imu
    # TODO: use Servo0 class to make adjustments based on imu
    #endregion
    
    #region camera commands
    # TODO use radio class to get a list of commands to execute
    # IDEA: use generator to iterate through commands, see yield and generator in python
    # for cmd in commands.
    print(commands.cmd_lst)
    commands.receive()
    print(commands.cmd_lst)
    
    # TODO: use servo 1 class to move camera
    # TODO: use camera class to take pictures and do filters
    #endregion
    
    #???: ability to re-adjust payload if IMU detects payload has shifted?


if __name__ == "__main__":
    main()
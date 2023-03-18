# main script that runs upon pi turn on
import time
from imu import IMU
from servo0 import Servo0
from servo1 import Servo1
from camera import Camera
from radioParser import RadioParser

def main():
    #region initialize components
    # imu
    imu = IMU()
    s0 = Servo0()
    s1 = Servo1()
    # TODO initialize DC motor class
    commands = RadioParser()
    cam = Camera()
    #endregion
    
    #region tests
    # imu test
    theta_DC,theta_0 = imu.GetAdjustments()
    print(theta_DC, theta_0)
    # s0.test()
    s1.test()
    # TODO hardware test DC motor
    cam.capture("class-test")
    #endregion
    
    # TODO: get servo accelerations and determine if rocket has landed or has moved during payload deployment
    
    #region deployment
    # TODO: use DC class to make adjustments based on imu
    # TODO: use Servo0 class to make adjustments based on imu
    s0.rotate(theta_0)
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
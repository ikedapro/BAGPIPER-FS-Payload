import math
import board
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX

class IMU:
    def __init__(self):
        self.i2c = board.I2C()

        self.sensor = ISM330DHCX(self.i2c)
        
    def debug(self):
        return "success"

    def GetAdjustments(self):
        [acc_x, acc_y, acc_z] = self.sensor.acceleration

        # TODO: The corresponding changes in angle seem to be correct however the
        # corresponding + / - signage of these values may need to be calibrated.

        # Angle along the Z-Axis of rotation needed to point up.
        theta_z = math.degrees(math.atan2(acc_x, acc_y))

        # Angle along the X-Axis of rotation needed to point up.

        # Uses the distance formula (a^2 + b^2 = c^2) to calculate length of "c"
        # between the acceleration values of x and y. This provides a constant
        # value when the payload is rotated along the Z-axis.
        c = math.sqrt(acc_x**2 + acc_y**2)

        # Determines the direction of the rotation since the distance formula only
        # outputs positive values.
        direction = 1 if acc_y < 0 else -1

        # Offset of 90 degrees since we actually want the payload to lay flat.
        offset_x = -math.pi / 2
        # between -90 and +90 is what we want to work with, otherwise tell DC motor to turn over

        theta_x = math.degrees(math.atan2(c * direction, acc_z) + offset_x)
        print(f"Angle Z: {theta_z} degrees, Angle X: {theta_x} degrees")
        # print("Acceleration: X: %.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
        # print("Gyro: X: %.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
        # print("")
        return [theta_z, theta_x]
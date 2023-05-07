import time
import board
import pulseio
from adafruit_motor import servo

# The v2 Camera has a horizontal field of view (fov) of 62.2 degrees 
# and a vertical fov of 48.8 degrees (link).
HORIZONTAL_FOV = 62.2
VERTICAL_FOV = 48.8


class HIIS_Gimbal:
    
    # -------------------------------------------------------------------------------
    # Class Functions

    def __init__(self, pan_pin=board.D18, tilt_pin=board.D17):
        self.m_pan_pin = tilt_pin
        self.m_tilt_pin = pan_pin
        self.m_pan_pwm = pulseio.PWMOut(self.m_pan_pin, duty_cycle=2 ** 15, frequency=50)
        self.m_tilt_pwm = pulseio.PWMOut(self.m_tilt_pin, duty_cycle=2 ** 15, frequency=50)
        self.m_pan_servo = servo.Servo(self.m_pan_pwm)
        self.m_tilt_servo = servo.Servo(self.m_tilt_pwm)
        self.armed = False


    def armGimbal(self):
        self.armed = True
        self.m_pan_servo.angle = 90
        self.m_tilt_servo.angle = 90


    def disarmGimbal(self):
        self.m_pan_servo.angle = 0
        self.m_tilt_servo.angle = 0
        self.armed = False


    def orientateGimbal(self, input_center_x, input_center_y, input_pixel_width, input_pixel_height):
        if self.armed is True:
            center_x = input_center_x
            center_y = input_center_y
            pixel_height = input_pixel_height
            pixel_width = input_pixel_width

            ang_x, ang_y = self.determineAngle(center_x, center_y, pixel_width, pixel_height)
            self.m_pan_servo.angle = ang_x
            self.m_tilt_servo.angle = ang_y


    def determineAngle(self, input_center_x, input_center_y, input_pixel_width, input_pixel_height):
        center_x = input_center_x
        center_y = input_center_y
        pixel_height = input_pixel_height
        pixel_width = input_pixel_width

        xRate = HORIZONTAL_FOV/pixel_width
        yRate = VERTICAL_FOV/pixel_height

        angle_x = xRate * center_x
        angle_y = yRate * center_y

        return [angle_x, angle_y]



if __name__ == '__main__':
    myGimbal = HIIS_Gimbal()
    myGimbal.armGimbal()
    time.sleep(3)
    myGimbal.disarmGimbal()
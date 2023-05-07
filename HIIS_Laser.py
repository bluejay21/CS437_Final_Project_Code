import time
import board
import digitalio

class HIIS_Laser:
    def __init__(self):
        self.m_laser_pin = digitalio.DigitalInOut(board.D21)
        self.m_laser_pin.direction = digitalio.Direction.OUTPUT

    def laserOn(self):
        self.m_laser_pin.value = True

    def laserOff(self):
        self.m_laser_pin.value = False
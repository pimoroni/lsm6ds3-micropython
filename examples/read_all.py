from machine import I2C
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
import time

# Create the I2C instance and pass that to LSM6DS3
i2c = I2C(0, scl=13, sda=12)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

# Grab and print the current readings once per second
while True:
    ax, ay, az, gx, gy, gz = sensor.get_readings()
    print("Accelerometer\nX:{}, Y:{}, Z:{}\nGyro\nX:{}, Y:{}, Z{}\n\n ".format(ax, ay, az, gx, gy, gz))
    time.sleep(1.0)

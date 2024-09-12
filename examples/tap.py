from machine import I2C
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
import time

# Create the I2C instance and pass that to LSM6DS3
i2c = I2C(0, scl=13, sda=12)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

# Print a string every time a tap is detected.
# You can use the function double_tap_detected() to detect only double taps
while True:

    if sensor.single_tap_detected():
        print("Single tap detected!")

    time.sleep(0.05)

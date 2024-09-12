from machine import I2C
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
import time

# Create the I2C instance and pass that to LSM6DS3
i2c = I2C(0, scl=13, sda=12)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

# Grab and print the current step count once per second
# You can also reset the step count by calling .reset_step_count()
while True:
    steps = sensor.get_step_count()
    print("Steps: {}".format(steps))
    time.sleep(1.0)

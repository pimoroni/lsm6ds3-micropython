# LSM6DS3TR-C MicroPython Library

The LSM6DS3TR-C is an always-on 3D accelerometer and 3D gyroscope that includes additional built-in functions such as:

- Pedometer
- Tap and double tap recognition
- Significant motion and tilt detection
- Free-fall detection

# Example Program
An example showing the basic setup and reading of the Gyro and Accelerometer. 

```
from machine import I2C
from lsm6ds3 import LSM6DS3, NORMAL_MODE_104HZ
import time

i2c = I2C(0, scl=13, sda=12)
sensor = LSM6DS3(i2c, mode=NORMAL_MODE_104HZ)

while True:
    ax, ay, az, gx, gy, gz = sensor.get_readings()
    print("Accelerometer\nX:{}, Y:{}, Z:{}\nGyro\nX:{}, Y:{}, Z{}\n\n ".format(ax, ay, az, gx, gy, gz))
    time.sleep(1.0)
```

# Functions

### `.get_readings()`

Get the current X Y Z values from the Accelerometer and Gyro. Returns `ax` `ay` `az` `gx` `gy` `gz`

#### Output:
```
>>> sensor.get_readings()
(-5839, -5124, -10199, 192, 12030, 24831)
```
### `.get_step_count()`
Get the current number of steps detected by the sensor. Returns an integer value.

#### Output:
```
>>> sensor.get_step_count()
29
```
### `.reset_step_count()`
Reset the step counter to 0

### `.tilt_detected()`
Returns `1` if the sensor detects tilt on the X Y or Z axis and `0` if no tilt detected.

### `.sig_motion_detected()`
Returns `1` if the sensor detects significant motion and `0` if no significant motion detected.

### `.single_tap_detected()`
Returns `1` if the sensor detects a single tap on the X Y or Z axis and `0` if no tap detected.

### `.double_tap_detected()`
Returns `1` if the sensor detects a double tap on the X Y or Z axis and `0` if no double tap detected.

### `.freefall_detected()`
Returns `1` if the sensor detects it is currently in free fall and `0` if no free fall detected.


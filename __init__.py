#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# The EV3 Brick
ev3 = EV3Brick()

# Drivebase motors
# B runs in the clockwise direction
# C runs in the anticlockwise direction and so needs to be reversed
leftmotor = Motor(Port.B)
rightmotor = Motor(Port.C, positivedirection = Direction.COUNTERCLOCKWISE)

# Functionality motors
forklftmotor = Motor(Port.A)
grabbermotor = Motor(Port.D)

# Ground light sensors
leftsensor = ColorSensor(Port.S1)
rightsensor = ColorSensor(Port.S2)

# Indicator Sensor (Light sensor that reads the indicators by each house)
indicatorsensor = ColorSensor(Port.S3)

# Gyro Sensor
gyrosensor = GyroSensor(Port.S4)

# Initializing the drivebase
robot = DriveBase(
    # The axle_track is the distance between the centres of the wheels/tyres
    # axle_track and wheel_diameter are measured in mm
    leftmotor,
    rightmotor,
    axle_track = 145,     # Measure and record actual values
    wheel_diameter = 51   # Measure and record actual values
)


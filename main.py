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

# Create your objects here.
ev3 = EV3Brick()

# Drivebase motors
leftmotor = Motor(Port.B)
rightmotor = Motor(Port.C, positivedirection = Direction.COUNTERCLOCKWISE)

# Functionality motors
forklftmotor = Motor(Port.A)
grabbermotor = Motor(Port.D)

# Grounded lightsensors
leftsensor = ColorSensor(Port.S1)
rightsensor = ColorSensor(Port.S2)

# Indicator Sensor
indicatorsensor = ColorSensor(Port.S3)

# Gyro Sensor
gyrosensor = GyroSensor(Port.S4)

# Kindly make sure all the specified ports are connected correctly before proceding.

# Initializing the drivebase
robot = DriveBase(
    # The axle_track is the distance between the centres of the wheels/tyres
    # axle_track and wheel_diameter are measured in mm
    leftmotor,
    rightmotor,
    axle_track = 145,     # Measure and record actual values
    wheel_diameter = 51   # Measure and record actual values
)


# The controller class. The controller class defines fucntions used for controlling the movements of the robot.
class Controller():
    def __init__(self, thresholdvalue):
        self.left_value = leftsensor.reflection()
        self.right_value = rightsensor.reflection()
        self.left_color = leftsensor.color()
        self.right_color = rightsensor.color()
        self.thresholdvalue = thresholdvalue
    
    def correctToLine(self, kp):
        return (self.self.left_value - self.self.right_value) * self.kp

    def onetwoonetwo(self, lightsensor, speed, kp):
        if lightsensor == leftsensor:
            return (self.thresholdvalue - rightsensor.reflection()) * self.kp
        else:
            return (self.thresholdvalue - leftsensor.reflection()) * self.kp


# The movement class. It inherits from the Controller class. It defines the movements of the robot on the game field.
class Movement(Controller):
    def __init__(self, speed):
        self.speed = speed
        self.distance = robot.distance()
    
    def follow1212(self, lightsensor):
        while lightsensor.color() != COLORS.Black:
            Controller().onetwoonetwo(lightsensor, self.speed, 2)       # Arbritrary value of kp

    def toLine(self, kp, distance):
        # Object of the controller class. AKA instance
        correction = Controller(12)                     # Threshold value is arbitrary. Measure and replace.
        while robot.distance <= distance:
            robot.drive(self.speed, correction.correctToLine(5))

class Inidicator():
    def __init__(self):
        self.indicatorcolors = [COLORS.Yellow, COLORS.Green, COLORS.Blue]
        self.readcolors = []                # read as in past tense
        colorlist = []

    def readIndicator(self):
        color = indicator_sensor.color()
        while color not in self.indicatorcolors:
            continue
        colorlist.append(color)            # Temporary storage for the colors
        if len(colorlist) == 2:
            self.readcolors.append(colorlist)
        return self.readcolors

    def getColorList(self,):
        pass

class Navigation():
    def __init__(self):
        pass


class Main():
    def __init__(self):
        print("Running...")
        # This is where everything is set
        pass

    def __run(self):
        pass

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
        self.left_color = leftsensor.color()
        self.right_color = rightsensor.color()
        self.thresholdvalue = thresholdvalue
    
    def correctToLine(self, kp):
        return (leftsensor.reflection() - rightsensor.reflection()) * self.kp

    def onetwoonetwo(self, lightsensor, speed, kp):
        if lightsensor == leftsensor:
            return (self.thresholdvalue - rightsensor.reflection()) * self.kp
        else:
            return (self.thresholdvalue - leftsensor.reflection()) * self.kp


# The movement class. It inherits from the Controller class. It defines the movements of the robot on the game field.
class Movement(Controller):
    def __init__(self, speed):
        self.speed = speed
        return None
    
    def follow1212(self, lightsensor):
      # Creating an object of the Controller class for the follow1212 function
      control = Controller(12) 
        while lightsensor.color() != COLORS.Black:
            robot.drive(self.speed, control.onetwoonetwo(lightsensor, self.speed, 2))      # Arbritrary value of kp

    def toLine(self, kp, distance):
        # Object of the controller class. AKA instance
        correction = Controller(12)                     # Threshold value is arbitrary. Measure and replace.
        while robot.distance <= distance:
            robot.drive(self.speed, correction.correctToLine(5))

class Inidicator():
    def __init__(self):
        self.indicatorcolors = [COLORS.Yellow, COLORS.Green, COLORS.Blue]
        self.readcolors = []                    # read as in past tense
        self.colorlist = []

    def readIndicator(self):
        color = indicatorsensor.color()
        while color not in self.indicatorcolors:
            color = indicatorsensor.color()
            continue
        self.colorlist.append(color)            # Temporary storage for the colors
        if len(self.colorlist) == 2:
            self.readcolors.append(self.colorlist)
            return self.readcolors
         self.readIndicator()

    def getcolorlist(self):
        pass


class Main():
    def __init__(self):
        print("Running...")
        # This is where everything is set
        pass

    def __run(self):
        for i in range(21):         # Arbitrary value - will during testing.
            if i == 0:
                # Start code.
                # Moving out of the start zone
                robot.straight(150)

                """
                Pseudocode:
                    > correct to line for 0.2 rotations with kp = 2 and speed = 5
                    > 1212 with sensor1 at 100 speed
                    > turn till sensor 2 senses the black line
                    > correct to line for 1 rotation with kp = 2.5 speed = 75
                """
            elif i = 1:`
                # Code that runs after the first junction
                """
                Pseudocode:
                    > 1212 at speed 100 with sensor 1
                    > turn clockwise until sensor 1 senses the black line
                    > turn clockwise until sensor 1 senses the white line
                    > correct to line at speed 75 for 0.75 rotations with kp = 5
                    > 1212 with sensor 1 at 100 speed
                """
            elif i = 2:
                # Code that runs after the second junction
                """
                
            elif i = 3:
                # Code that runs after the third junction
            elif i = 4:
                # Code that runs after the fourth junction
            elif i = 5:
                # Code that runs after the fifth junction
            elif i = 6:
                # Code that runs after the sixth junction
            elif i = 7:
                # Code that runs after the seven junction
            elif i = 8:
                # Code that runs after the eigth junction
            elif i = 9:
                # Code that runs after the ninth junction
            elif i = 10:
                # Code that runs after the tenth junction
            elif i = 11:
                # Code that runs after the eleventh junction
            elif i = 12:
                # Code that runs after the twelth junction
            elif i = 13:
                # Code that runs after the thirteenth junction
            elif i = 14:
                # Code that runs after the fourteenth junction
            elif i = 15:
                # Code that runs after the fifteenth junction
            elif i = 16:
                # Code that runs after the sixteenth junction
            elif i = 17:
                # Code that runs after the seventeenth junction
            elif i = 18:
                # Code that runs after the eigteenth junction
            elif i = 19:
                # Code that runs after the nineteenth junction
            elif i = 20:
                # Code that runs after the twentieth junction

             else:
                 # Kinda like the default case for the "switch statement"
                 # I'm using "" because its not actually a switch statement   
            

if __name__ = '__main__':
    Main().__run()

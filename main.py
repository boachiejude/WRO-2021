#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from Movement import *

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
    wheel_diameter = 6
)
robot.settings(straight_acceleration = 75)


# DEFINE
class Main():
    def __init__(self):
        print("Running...")
        self.move = Movement(50)
        return None

    def run(self):
        for i in range(21):         # Arbitrary value - will during testing.
            if i == 0:
                # Start code.
                # Moving out of the start zone
                robot.straight(150)
                # correct to line for 0.2 rotations with kp = 2 and speed = 50
                self.move.toLine(2, 10)
                print("hjk")
                # 1212 with sensor1 at 100 speed
                self.move.follow1212(leftsensor)
                # turn till sensor 2 senses the black line
                self.move.turnUntil(leftsensor, Color.BLACK)
                
            elif i == 1:
                # Code that runs after the first junction
                # Correct to line for 1 rotation with kp = 2.5 speed = 75
                self.move.toLine(2.5, 10)
                # 1212 at speed 100 with sensor 1
                self.move.follow1212(leftsensor)
                # turn clockwise until sensor 1 senses the black line
                self.move.turnUntil(leftsensor, Color.BLACK)
                # turn clockwise until sensor 1 senses the white line
                self.move.turnUntil(leftsensor, Color.WHITE)
                # correct to line at speed 75 for 0.75 rotations with kp = 5
                self.move.toLine(5, 10)
                # 1212 with sensor 1 at 100 speed
                self.move.follow1212(leftsensor)

            elif i == 2:
                # Code that runs after the second junction
                robot.straight(18.85)        
                robot.straight(-18.85)       
                forkliftmotor.run_angle(1980)
                robot.straight(-10.37)
                forkliftmotor.run_angle(-1980)
                robot.straight(-16.02)
                self.move.turnUntil(rightsensor, Color.WHITE)
                self.move.turnUntil(rightsensor, Color.BLACK)
                self.move.turnUntil(rightsensor, Color.WHITE)
                self.move.toLine(5, 1.88)

            elif i == 3:
                # Code that runs after the third junction
                # This is the part of the code where the robot picks up the wind units
                self.move.pickWindUnits()

            elif i == 5:
                # Code that runs after the fifth junction
                # Turn right
                self.move.turnUntil(rightsensor, Color.BLACK)
                self.move.toLine(3, 10)

            elif i == 6:
                # Code that runs after the sixth junction
                self.move.turnUntil(leftsensor, Color.BLACK)
                self.move.turnUntil(leftsensor, Color.WHITE)
                self.move.turnUntil(leftsensor, Color.BLACK)
                self.move.pickHydroUnits()

            elif i == 7:
                # Code that runs after the seven junction
                pass

            elif i == 8:
                # Code that runs after the eigth junction
                pass

            elif i == 9:
                # Code that runs after the ninth junction
                pass

            elif i == 10:
                # Code that runs after the tenth junction
                pass

            elif i == 11:
                # Code that runs after the eleventh junction
                pass

            elif i == 12:
                # Code that runs after the twelth junction
                pass

            elif i == 13:
                # Code that runs after the thirteenth junction
                pass

            elif i == 14:
                # Code that runs after the fourteenth junction
                pass

            elif i ==15:
                # Code that runs after the fifteenth junction
                pass

            elif i == 16:
                # Code that runs after the sixteenth junction
                pass

            elif i == 17:
                # Code that runs after the seventeenth junction
                pass

            elif i == 18:
                # Code that runs after the eigteenth junction
                pass

            elif i == 19:
                # Code that runs after the nineteenth junction
                pass

            elif i == 20:
                # Code that runs after the twentieth junction
                pass

            else:
                # Kinda like the default case for the "switch statement"
                # I'm using "" because its not actually a switch statement   
                continue
            # code that runs anyway:
            print(i)
            robot.reset()

# EXECUTE
if __name__ == '__main__':
    Main().run()


# Starting: brickrun --directory="/home/robot/myproj" "/home/robot/myproj/main.py"
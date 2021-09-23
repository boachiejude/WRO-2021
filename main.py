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


# The Controller class. The Controller class defines fucntions used for controlling the movements of the robot.
class Controller():
    def __init__(self, thresholdvalue):
        # self.left_color = leftsensor.color()
        # self.right_color = rightsensor.color()
        self.thresholdvalue = thresholdvalue
    
    def correctToLine(self, kp):
        return (leftsensor.reflection() - rightsensor.reflection()) * kp

    def onetwoonetwo(self, lightsensor, kp):
        if lightsensor == leftsensor:
            return (self.thresholdvalue - rightsensor.reflection()) * kp
        else:
            return (self.thresholdvalue - leftsensor.reflection()) * kp


class Indicator():
    def __init__(self):
        self.indicatorcolors = [COLORS.Yellow, COLORS.Green, COLORS.Blue]
        self.readcolors = []                    # "read" as in past tense
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

    def getColorlist(self):
        return self.readcolors


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

    def turnUntil(self,sensor, color):
        while sensor.color() != color:
            robot.drive(self.speed, 50)
        robot.stop()

    def pickWindUnits(self):
        pass

    def pickHydroUnits(self):
        pass

    def serve(self):
        houseIndicator = Indicator()
        houseIndicator.readIndicator()
        robot.reset()
        for i in houseIndicator.getColorList():
            if i == COLORS.Green:
                # Drop the green units
                pass
            elif i == COLORS.Yellow:
                # Drop the yellow units from the grabber
                pass
            elif i == COLORS.Blue:
                # Drop blue units
                pass
            else:
                # Drop surplus units
                pass
            
            # Just a little code here to make the robot go back to the original position it was in

class Main():
    def __init__(self):
        print("Running...")
        # This is where everything is set
        self.move = Movement(50)
        pass

    def __run(self):
        for i in range(21):         # Arbitrary value - will during testing.
            if i == 0:
                # Start code.
                # Moving out of the start zone
                robot.straight(150)
                # correct to line for 0.2 rotations with kp = 2 and speed = 50
                self.move.toLine(2, 10)
                # 1212 with sensor1 at 100 speed
                self.move.follow1212(leftsensor)
                # turn till sensor 2 senses the black line
                self.move.turnUntil(leftsensor, COLORS.Black)
                
            elif i == 1:
                # Code that runs after the first junction
                # Correct to line for 1 rotation with kp = 2.5 speed = 75
                self.move.toLine(2.5, 10)
                # 1212 at speed 100 with sensor 1
                self.move.follow1212(leftsensor)
                # turn clockwise until sensor 1 senses the black line
                self.move.turnUntil(leftsensor, COLORS.Black)
                # turn clockwise until sensor 1 senses the white line
                self.move.turnUntil(leftsensor, COLORS.White)
                # correct to line at speed 75 for 0.75 rotations with kp = 5
                self.move.toLine(5, 10)
                # 1212 with sensor 1 at 100 speed
                self.move.follow1212(leftsensor)

            elif i == 2:
                # Code that runs after the second junction
                """
                Pseudocode:
                    move forward for 1 rotation,
                    backward for 0.28 rotations
                    forklift motor run at 100 speed for 5.6 rotations
                    move backward at 50 percent speed for 0.55 rotations(down)
                    forklift motor run at 100 speed for -5.5 rotations(up)
                    move backward for 0.85 rotations at 100 percent power
                    turn till sensor 2 senses white
                    turn till sensor 2 senses black
                    turn till sensor 2 senses white
                    correct to line for 0.1 rotations at 50 percent with kp = 5
                """
            elif i == 3:
                # Code that runs after the third junction
                
                # This is the part of the code where the robot picks up the wind units
                # Code for picking up wind units
                pass

            elif i == 4:
                # Code that runs after the fourth junction
                pass

            elif i == 5:
                # Code that runs after the fifth junction
                pass

            elif i == 6:
                # Code that runs after the sixth junction
                pass

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
                pass

if __name__ == '__main__':
    Main().__run()

from __init__ import *
from Indicator import *
from Controller import *

# The movement class. It inherits from the Controller class. It defines the kinds of movements of the robot on the game field.
class Movement(Controller):
    def __init__(self, speed):
        self.speed = speed
        return None
    
    def follow1212(self, lightsensor):
        # Creating an object of the Controller class for the follow1212 function
        control = Controller(12) 
        while lightsensor.color() != Color.BLACK:
            robot.drive(self.speed, control.onetwoonetwo(lightsensor, self.speed, 2))      # Arbritrary value of kp

    def toLine(self, kp, distance):
        # Instance of the controller class.
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

    def specialDelivery(self):
        houseIndicator = Indicator()
        houseIndicator.readIndicator()
        robot.reset()
        for i in houseIndicator.getColorList():
            if i == Color.GREEN:
                # Drop the green units
                forklftmotor.run_angle(1980)
                robot.straight(-5)              # How much the robot will come back after dropping the front two units in order to release it
                forkliftmotor.run_angle(-1980)
                continue
            elif i == Color.YELLOW:
                # Drop the yellow units from the grabber
                forkliftmotor.run_angle(1900)
                grabbermotor.run_target(100)
                forkliftmotor.run_angle(-1900)
                grabbermotor.run_target(0)
                pass
            elif i == Color.BLUE:
                # Drop blue units
                robot.turn(100)         # Supposed to turn the robot 180 degrees
                forklftmotor.run_angle(1980)
                robot.straight(-5)              # How much the robot will come back after dropping the front two units in order to release it
                forkliftmotor.run_angle(-1980)
                pass
            else:
                # Drop surplus units
                pass
            
            # Just a little code here to make the robot go back to the original position it was in

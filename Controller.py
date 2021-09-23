from __init__ import *

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
from __init__ import *

class Indicator():
    def __init__(self):
        self.indicatorcolors = [Color.YELLOW, Color.GREEN, Color.BLUE, None]
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


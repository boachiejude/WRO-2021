from __init__ import *
import Movement

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
                self.move.turnUntil(leftsensor, Color.Black)
                
            elif i == 1:
                # Code that runs after the first junction
                # Correct to line for 1 rotation with kp = 2.5 speed = 75
                self.move.toLine(2.5, 10)
                # 1212 at speed 100 with sensor 1
                self.move.follow1212(leftsensor)
                # turn clockwise until sensor 1 senses the black line
                self.move.turnUntil(leftsensor, Color.Black)
                # turn clockwise until sensor 1 senses the white line
                self.move.turnUntil(leftsensor, Color.White)
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

# EXECUTE
if __name__ == '__main__':
    Main().__run()

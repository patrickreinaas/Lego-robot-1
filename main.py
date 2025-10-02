#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""


from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Prints Hello World on the robots screen
ev3.screen.print("Hello World")
ev3.speaker.beep()
#Waits 3 seconds
wait(3000)

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=118)

#Drive forward 10 cm
robot.straight(100)
ev3.speaker.beep()

#Turn 90 degrees clockwise
robot.turn(90)
ev3.speaker.beep()

#Drive forward 15 cm
robot.straight(150)
ev3.speaker.beep()

#Turn 90 degrees clockwise
robot.turn(90)
ev3.speaker.beep()

#Drive forward 10 cm
robot.straight(100)
ev3.speaker.beep()

#Turn 90 degrees clockwise
robot.turn(90)
ev3.speaker.beep()

#Drive forward 15 cm
robot.straight(150)
ev3.speaker.beep()

#Makes the robot say "Have a nice day"
ev3.speaker.say("Have a nice day")

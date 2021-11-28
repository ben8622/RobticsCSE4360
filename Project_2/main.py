#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import constants as const


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Initialize Sensors & Motors
nxt_sensor = LightSensor(Port.S1)
ev3_sensor = ColorSensor(Port.S4)
us_sensor = UltrasonicSensor(Port.S2)
left_motor = Motor(Port.D)
right_motor = Motor(Port.C)

# Used to make robot wander a bigger and bigger circle
# until a straight line is done
wander_counter = 0
going_straight = 0

# Behavior functions
def wander():
  global wander_counter
  global going_straight
  left_motor.run(-200 )
  right_motor.run(-50 - wander_counter)

  # Radius of our circle gets biger until
  # we are driving straight, then we drive
  # straight for 1 seconds (5ms * 200 = 2s)
  if(wander_counter >= 150):
    going_straight += 1
  else:
    wander_counter = wander_counter + .1
  if(going_straight == 200):
    wander_counter = 0

def stop():
  left_motor.stop()
  right_motor.stop()
  left_motor.hold()
  right_motor.hold()

def found_wall():
  nxt_reflection = nxt_sensor.reflection()
  ev3_reflection = ev3_sensor.reflection()
  return (nxt_reflection  <= const.NXT_DETECT)

def follow_wall():
  if(found_wall()):
    right_motor.stop()
    left_motor.run(-100)

    if(found_wall()):
      while found_wall():
        right_motor.run(100)
      right_motor.stop()

  else:
    left_motor.stop()
    right_motor.run(-100)

ev3.speaker.say("Starting program")

wait_time = 300 #not using this yet
goal_reached = False
wall_found = False
inches_const = 25.4

#this gives distance in inches
#us_sensor.distance() / 25.4

while not goal_reached:
  if(found_wall()):
    stop()
    ev3.speaker.say("Wall Found")
    wall_found = True

    while wall_found:
      follow_wall()
    
  else:
    wander()

  wait(10)


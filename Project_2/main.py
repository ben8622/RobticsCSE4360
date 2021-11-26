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
left_motor = Motor(Port.D)
right_motor = Motor(Port.C)

# Used to make robot wander a bigger and bigger circle
# until a straight line is done
wander_counter = 0

# Behavior functions
def wander():
  left_motor.run(-200 + wander_counter)
  right_motor.run(-50)
  if( wander_counter == 150 ):
    wander_counter = 0
  else:
    wander_counter += 1
def stop():
  left_motor.stop()
  right_motor.stop()
  left_motor.hold()
  right_motor.hold()


ev3.speaker.say("Starting program")

while True:
  nxt_reflection = nxt_sensor.reflection()
  ev3_reflection = ev3_sensor.reflection()

  if(nxt_reflection  <= const.NXT_DETECT):
    stop()
    ev3.speaker.say("Wall Found")
  else:
    wander()

  wait(5)
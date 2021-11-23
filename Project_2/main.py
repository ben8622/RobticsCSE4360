#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Initialize Sensors
nxt_sensor = LightSensor(Port.S1)
ev3_sensor = ColorSensor(Port.S4)


# Write your program here.
ev3.speaker.say("Starting program")

while True:
  nxt_reflection = nxt_sensor.reflection()
  ev3_reflection = ev3_sensor.reflection()

  ev3.screen.print("nxt_reflection = " + str(nxt_reflection))
  ev3.screen.print("ev3_reflection = " + str(ev3_reflection))

  wait(100)
  ev3.screen.clear()
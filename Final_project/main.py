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


# Create your objects here.
ev3 = EV3Brick()
elevator = Motor(Port.A)


# Write your program here.
ev3.speaker.beep()

while(True):
  if(ev3.buttons.pressed() == [Button.UP]):
    elevator.run_time(500, 5000, Stop.HOLD, True)
  elif(ev3.buttons.pressed() == [Button.DOWN]):
    elevator.run_time(-500, 5000, Stop.HOLD, True)

  ev3.screen.print(ev3.buttons.pressed())
  

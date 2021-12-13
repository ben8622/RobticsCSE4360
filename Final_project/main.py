#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import wait
from pybricks.nxtdevices import LightSensor



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
elevator = Motor(Port.C)
touch_sens = TouchSensor(Port.S2)
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
color_sens = ColorSensor(Port.S1)
light_sens = LightSensor(Port.S4)
gyro_sens = GyroSensor(Port.S3, Direction.CLOCKWISE)


# Write your program here.
ev3.speaker.beep()

while(True):
  # print(color_sens.color())
  # print(gyro_sens.angle())
  # print(light_sens.reflection())


  if(touch_sens.pressed()):
    print("pressed!")
    elevator.run_time(-200, 5000, Stop.HOLD, True)
    # left_motor.run(100)
    # right_motor.run(100)
    # wait(1000)
    # left_motor.stop()
    # right_motor.stop()

  if(ev3.buttons.pressed() == [Button.UP]):
    elevator.run_time(1000, 5000, Stop.HOLD, True)

  elif(ev3.buttons.pressed() == [Button.DOWN]):
    elevator.run_time(-1000, 5000, Stop.HOLD, True)

  ev3.screen.print(ev3.buttons.pressed())
  

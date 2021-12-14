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
gyro_sens = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)


# Methods
def move_forward():
  left_motor.run(100)
  right_motor.run(100)

def stop_motors():
  left_motor.stop()
  right_motor.stop()

def read_gyro():
  return gyro_sens.angle()

def elevator_up():
  elevator.run(-200)
  wait(2000)
  elevator.stop()

def elevator_down():
  elevator.run(200)
  wait(2000)
  elevator.stop()
  
# Write your program here.
ev3.speaker.beep()


while(True):
  # print(color_sens.color())
  print(gyro_sens.angle())
  # print(light_sens.reflection())

  move_forward()

  # if(read_gyro() > 0):
  #   elevator_up()

  if(read_gyro() <= 0):
    gyro_sens.reset_angle(0)
    #elevator_down()  

    # left_motor.run(100)
    # right_motor.run(100)
    # wait(1000)
    # left_motor.stop()
    # right_motor.stop()

  ev3.screen.print(gyro_sens.angle())

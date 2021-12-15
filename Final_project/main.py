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
rear_motor = Motor(Port.B)
color_sens = ColorSensor(Port.S1)
ultrasonic_sens = UltrasonicSensor(Port.S4)
gyro_sens = GyroSensor(Port.S3, Direction.CLOCKWISE)


# Methods
def is_pressed():
  return touch_sens.pressed()

def rear_motor_forward(velocity = 100):
  rear_motor.run(-1 * velocity)

def move_forward(velocity = 100):
  left_motor.run(velocity)
  right_motor.run(velocity)
  rear_motor_forward(velocity)

def stop_all_motors():
  left_motor.stop()
  right_motor.stop()
  rear_motor.stop()
  elevator.stop()

def read_gyro():
  return gyro_sens.angle()

def elevator_up(time = 4000):
  elevator.run(-350)
  wait(time)
  elevator.stop()

def elevator_down(time = 4000):
  elevator.run(350)
  wait(time)
  elevator.stop()


def zero_elevator():
  elevator.run(-250)
  while(not is_pressed()):
    continue
  elevator.stop()
  elevator.run_time(250, 9000, Stop.HOLD, True)
  gyro_sens.reset_angle(0)

def check_if_end():

  stop_all_motors()
  time = 0
  while(time < 1500):
    if(ultrasonic_sens.distance() > 600):
      ev3.speaker.say("End of stairs")
      return True
    time += 5
    wait(5)

  return False
    

  
# Write your program here.
ev3.speaker.beep()

# zero_elevator()

# elevator_moving = False

# while(True):

#   if(read_gyro() > 10 and not elevator_moving):
#     ev3.speaker.beep()
#     elevator_up()
#     elevator_down()
#     if check_if_end():
#       break

#   move_forward()

# ev3.speaker.say("Going down stairs")
# elevator_up(3000)

while(True):
#   move_forward(-100)
  ev3.screen.print(str(color_sens.color()))
  # print("test")


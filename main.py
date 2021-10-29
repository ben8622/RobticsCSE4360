#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
import constant

# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

def turn_right(ms):
  left_motor.run_time(-100, ms, Stop.HOLD, False)
  right_motor.run_time(100, ms, Stop.HOLD, True)
def turn_left(ms):
  left_motor.run_time(100, ms, Stop.HOLD, False)
  right_motor.run_time(-100, ms, Stop.HOLD, True)
def move_forward(ms):
  left_motor.run_time(250, ms, Stop.HOLD, False)
  right_motor.run_time(250, ms, Stop.HOLD, True)
def move_backward(ms):
  left_motor.run_time(-250, ms, Stop.HOLD, False)
  right_motor.run_time(-250, ms, Stop.HOLD, True)

# class Node:
#   def __init__(self):
#     self.x = 0.0
#     self.y = 0.0
#     self.is_object = False
#     self.visited = False

#   def set_xy(self, x, y):
#     self.x = x
#     self.y = y

#   def set_visited(self):
#     self.visited = True

#   def set_is_object(self):
#     self.is_object = True



# Sound to signify start
ev3.speaker.beep()

# Play another beep sound.
ev3.speaker.beep(1000, 500)

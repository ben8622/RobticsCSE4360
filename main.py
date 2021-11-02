#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
import constant
import time
import Classes

# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
ev3.speaker.beep(500, 450)
offset = 4

def turn_right():
  left_motor.run_time(-constant.TURN_SPEED, constant.TURN_TIME, Stop.HOLD, False)
  right_motor.run_time(constant.TURN_SPEED-offset, constant.TURN_TIME, Stop.HOLD, True)
def turn_left():
  left_motor.run_time(constant.TURN_SPEED, constant.TURN_TIME, Stop.HOLD, False)
  right_motor.run_time(-constant.TURN_SPEED+offset, constant.TURN_TIME, Stop.HOLD, True)
def move_forward():
  left_motor.run_time(constant.MOVE_SPEED, constant.MOVE_TIME, Stop.HOLD, False)
  right_motor.run_time(constant.MOVE_SPEED-offset, constant.MOVE_TIME, Stop.HOLD, True)
def move_backward(ms):
  left_motor.run_time(-250, ms, Stop.HOLD, False)
  right_motor.run_time(-250, ms, Stop.HOLD, True)

def perform_commands(commands):
  for command in commands:
    if(command == "turn_right"): turn_right()
    elif(command == "turn_left"): turn_left()
    elif(command == "move"): move_forward()

map = Classes.Map()
map.set_obstacles()
map.set_start_and_goal()
map.set_man_values()

# Sound to signify start
ev3.speaker.beep()

move_forward()
time.sleep(1)

turn_right()
time.sleep(1)

turn_left()
time.sleep(1)

# while(not map.visited_goal()):
#   commands = map.next_node()
#   perform_commands(commands)

# Play another beep sound.
ev3.speaker.beep(1000, 500)

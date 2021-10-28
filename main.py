#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction

# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
left_motor_cw = Motor(Port.D)
right_motor_cw = Motor(Port.A)

def turn_right(ms):
  left_motor_cw.run_time(-100, ms, Stop.HOLD, False)
  right_motor_cw.run_time(100, ms, Stop.HOLD, True)
def turn_left(ms):
  left_motor_cw.run_time(100, ms, Stop.HOLD, False)
  right_motor_cw.run_time(-100, ms, Stop.HOLD, True)
def move_forward(ms):
  left_motor_cw.run_time(250, ms, Stop.HOLD, False)
  right_motor_cw.run_time(250, ms, Stop.HOLD, True)
def move_backward(ms):
  left_motor_cw.run_time(-250, ms, Stop.HOLD, False)
  right_motor_cw.run_time(-250, ms, Stop.HOLD, True)



# Play a sound.
ev3.speaker.beep()
# 1800 @ 100 speed seems to be right angle
turn_right(2630)
# turn_right(2630)
# turn_right(2630)
# turn_right(2630)
# turn_left(2620) ## always overshoots more than turn_right?
# turn_left(5000)
# move_forward(5000)
# move_backward(5000)

# Play another beep sound.
ev3.speaker.beep(1000, 500)

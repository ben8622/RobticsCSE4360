#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait
import constants as const

ev3 = EV3Brick()

# Initialize Sensors & Motors
nxt_sensor = LightSensor(Port.S1)
ev3_sensor = ColorSensor(Port.S4)
us_sensor = UltrasonicSensor(Port.S2)
left_motor = Motor(Port.D)
right_motor = Motor(Port.C)

# Global variables used throughout to change state
wander_counter = 0
going_straight = 0
time_passed = 0
time_last_checked = 0
goal_found = False
found_wall = False
inches_const = 25.4

##############################
##### BEHAVIOR FUNCTIONS #####
##############################
def wander():
  global wander_counter
  global going_straight
  global found_wall

  # Radius of our circle gets biger until
  # we are driving straight, then we drive
  # straight for 1 seconds (5ms * 200 = 2s)
  if(wander_counter >= 150):
    going_straight += 1
  else:
    wander_counter = wander_counter + 1
  if(going_straight == 200):
    wander_counter = 0
    going_straight = 0

  left_motor.run(-200 )
  right_motor.run(-50 - wander_counter)

  if(found_wall_left()):
    found_wall = True
    stop()
    ev3.speaker.say("Wall found on left side")
  elif(found_wall_right()):
    found_wall = True
    stop()
    ev3.speaker.say("Wall found on right side")
    turn_90_right()
def start_wander():
  left_motor.run_time(-const.TURN_SPEED_180, const.TURN_TIME_90, Stop.HOLD, False)
  right_motor.run_time(const.TURN_SPEED_180, const.TURN_TIME_90, Stop.HOLD, True)

  time_passed = 0
  while(not(found_wall_left() or found_wall_right()) and (time_passed < 2000)):
    left_motor.run(-150)
    right_motor.run(-150)
    time_passed += 10
    wait(10)
  stop()
def found_wall_left():
  nxt_reflection = nxt_sensor.reflection()
  return (nxt_reflection  <= const.NXT_DETECT)
def found_wall_right():
  ev3_reflection = ev3_sensor.reflection()
  return (ev3_reflection  <= const.EV3_DETECT)
def follow_wall():
  if(found_wall_left()):
    right_motor.stop()
    left_motor.run(-200)

    if(found_wall_left()):
      while found_wall_left():
        right_motor.run(200)
      right_motor.stop()

  else:
    left_motor.stop()
    right_motor.run(-200)
    
##############################
##### MOVEMENT FUNCTIONS #####
##############################
def stop():
  left_motor.stop()
  right_motor.stop()
  left_motor.hold()
  right_motor.hold()
def turn_180_right():
  left_motor.run_time(-const.TURN_SPEED_180, const.TURN_TIME_180, Stop.HOLD, False)
  right_motor.run_time(const.TURN_SPEED_180, const.TURN_TIME_180, Stop.HOLD, True)
def turn_180_left():
  left_motor.run_time(const.TURN_SPEED_180, const.TURN_TIME_180, Stop.HOLD, False)
  right_motor.run_time(-const.TURN_SPEED_180, const.TURN_TIME_180, Stop.HOLD, True)
def turn_90_right():
  left_motor.run_time(-const.TURN_SPEED_180, const.TURN_TIME_90, Stop.HOLD, False)
  right_motor.run_time(const.TURN_SPEED_180, const.TURN_TIME_90, Stop.HOLD, True)
def turn_90_left():
  left_motor.run_time(const.TURN_SPEED_180, const.TURN_TIME_90, Stop.HOLD, False)
  right_motor.run_time(-const.TURN_SPEED_180, const.TURN_TIME_90, Stop.HOLD, True)

##############################
####### GOAL FUNCTIONS #######
##############################
def detect_goal():
  global goal_found
  distance = us_sensor.distance() / 25.4
  color = ev3_sensor.color()
  goal_found =  color == Color.RED or distance <= 14
  return goal_found
def check_for_goal():
  time = 0
  while(time < const.TURN_TIME_180 and not detect_goal()):
    left_motor.run(-75)
    right_motor.run(75)
    time += 5
    wait(5)

  stop()
  time = 0

  while(time < const.TURN_TIME_180 and not detect_goal()):
    left_motor.run(75)
    right_motor.run(-75)
    time += 5
    wait(5)
  
  stop()
def face_goal():
  turn_90_right()
  time = 0
  min_distance = 100
  i=0

  # Scans 180 degrees to find the closest distance
  while(time < 3750):
    if( (us_sensor.distance() / 25.4) < min_distance):
      stop()
      min_distance = us_sensor.distance() / 25.4

    left_motor.run(35)
    right_motor.run(-35)
    time += 5
    wait(5)
  stop()
  time = 0
  while(time < 3750):
    if( (us_sensor.distance() / 25.4) < min_distance):
      stop()
      min_distance = us_sensor.distance() / 25.4
    left_motor.run(-35)
    right_motor.run(35)
    time += 5
    wait(5)
  stop()
  time = 0

  ## Faces the object
  time = 0
  curr_distance = 0
  threshold = .25
  while(not (abs(min_distance - curr_distance) < threshold)):
      # Threshold doubles every 5 seconds not found
      if(time > 5000):
        time = 0
        threshold = threshold * 2
      curr_distance = us_sensor.distance() / 25.4
      left_motor.run(40)
      right_motor.run(-40)
      time += 5
      wait(5)
  stop()
  
  return min_distance


ev3.speaker.say("Starting program")

# Wander until a wall is found, then wall follow checking for the object/goal every 3 seconds
while not goal_found:
  if(found_wall):
    follow_wall()
  else:
    wander()

  ## Check for goal every 3 seconds
  if(time_last_checked > 3000):
    check_for_goal()
    time_last_checked = 0

  time_last_checked +=  5
  wait(5)

# Stop after goal is found
stop()
ev3.speaker.say("Goal found!")

# Orient robot to face the object
face_goal()

# Move about 1.5 feet to displace the object
left_motor.run_time(-200, 5250, Stop.HOLD, False)
right_motor.run_time(-200, 5250, Stop.HOLD, True)


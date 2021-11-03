NINETY_DEGREE_TURN = 2600 # miliseconds

METERS_TO_FEET = 3.2808

# Node for every half foot
#ROWS = 10
ROWS = 20
#COLS = 16
COLS = 32
OBSTACLES = [
  (0.61, 2.743),(0.915, 2.743),(1.219, 2.743),
  (1.829, 1.219),(1.829, 1.524),( 1.829, 1.829), 
  (1.829, 2.134),(2.743, 0.305),(2.743, 0.61),
  (2.743, 0.915),(2.743, 2.743),(3.048, 2.743),
  (3.353, 2.743),(-1,-1),(-1,-1),
  (-1,-1),(-1,-1),(-1,-1),
  (-1,-1),(-1,-1),(-1,-1),
  (-1,-1),(-1,-1),(-1,-1),
  (-1,-1)]

# GOAL = (2.134, 0.305)
GOAL = (3.658, 1.829)
# START = (0.305, 1.219)
START = (0.305, 1.219)

TURN_TIME = 2050
TURN_SPEED = 100

#MOVE_TIME = 2650
MOVE_TIME = 1950
MOVE_SPEED = 200

TEST_OBSTACLES = [(1.219, 0.61), (1.372, 0.61), (1.524, 0.763),(1.524, 0.915), (1.524, 1.068), (1.524, 1.219), (1.524, 1.372)]
# half foot = 0.1525 meters
EAST = 'e'
NORTH = 'n'
WEST = 'w'
SOUTH = 's'

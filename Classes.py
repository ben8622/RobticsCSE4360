import constant

class Node:
  def __init__(self):
    self.x = 0.0
    self.y = 0.0
    self.is_obstacle = False
    self.visited = False
    self.is_start = False
    self.is_goal = False

  def set_xy(self, x, y):
    self.x = x
    self.y = y

  def set_visited(self):
    self.visited = True

  def set_is_obstacle(self):
    self.is_obstacle = True

  def set_is_start(self):
    self.is_start = True

  def set_is_goal(self):
    self.is_goal = True

  def build_empty_map(self):
    empty_map = []
    for i in range(constant.ROWS):
      empty_row = []
      for j in range(constant.COLS):
        empty_row.append(Node())
      empty_map.append(empty_row)
    return empty_map

class Map:
  def __init__(self):
    self.map = []
    for i in range(constant.ROWS):
      empty_row = []
      for j in range(constant.COLS):
        node = Node()
        x = .5 * j
        y = .5 * (constant.ROWS - i)
        node.set_xy(x, y)
        empty_row.append(node)
      self.map.append(empty_row)
      
  def print_map_coords(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        print(f'({self.map[i][j].x},{self.map[i][j].y})', end="")
      print("")

  def print_obstacle_map(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        is_obstacle = 1 if self.map[i][j].is_obstacle else 0
        print(f'(   {is_obstacle}   )', end="")
      print("")

  def print_start_and_goal_map(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        temp = 1 if self.map[i][j].is_start or self.map[i][j].is_goal else 0
        print(f'(   {temp}   )', end="")
      print("")

  def print_complete_map(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        temp = ' '
        if(self.map[i][j].is_obstacle): temp = 'O'
        elif(self.map[i][j].is_start): temp = 'S'
        elif(self.map[i][j].is_goal): temp = 'G'
        print(f'[ {temp} ]', end="")
      print("")

  def set_obstacles(self):
    for obstacle in constant.TEST_OBSTACLES:
      if obstacle[0] == -1: continue
      obs_x = round(obstacle[0] * constant.METERS_TO_FEET, 2)
      obs_y = round(obstacle[1] * constant.METERS_TO_FEET, 2)
      for row in self.map:
        for node in row:
          if(node.x == obs_x and node.y == obs_y):
            node.set_is_obstacle()

  def set_start_and_goal(self):
    start = ( round(constant.START[0] * constant.METERS_TO_FEET, 2), round(constant.START[1] * constant.METERS_TO_FEET, 2) )
    goal = ( round(constant.GOAL[0] * constant.METERS_TO_FEET, 2), round(constant.GOAL[1] * constant.METERS_TO_FEET, 2) )
    for row in self.map:
      for node in row:
        if((node.x, node.y) == start):
          node.set_is_start()
        elif((node.x, node.y) == goal):
          node.set_is_goal()

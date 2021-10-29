import constant

class Node:
  def __init__(self):
    self.x = 0.0
    self.y = 0.0
    self.is_object = False
    self.visited = False

  def set_xy(self, x, y):
    self.x = x
    self.y = y

  def set_visited(self):
    self.visited = True

  def set_is_object(self):
    self.is_object = True

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
      
  def print_map(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        print(f'({self.map[i][j].x},{self.map[i][j].y})', end="")
      print("")

  def add_obstacles(self):
    for obstacle in constant.OBSTACLES:
      if obstacle[0] == -1: continue
      obs_x = round(obstacle[0] * constant.METERS_TO_FEET, 2)
      obs_y = round(obstacle[1] * constant.METERS_TO_FEET, 2)
      print(f'({obs_x},{obs_y})')
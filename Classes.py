import constant 
import copy ## used to deep copy an object otherwise it is copied by reference

class Node:
  def __init__(self):
    self.x = 0.0
    self.y = 0.0
    self.man_val = None
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
    self.man_val = -1

  def set_is_start(self):
    self.is_start = True
    self.visited = True;

  def set_is_goal(self):
    self.is_goal = True
    self.man_val = 0

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
    self.start = None
    self.goal = None
    self.start_ij = None
    self.goal_ij = None
    self.curr_ij = None
    self.curr_dir = constant.EAST
    for i in range(constant.ROWS):
      empty_row = []
      for j in range(constant.COLS):
        node = Node()
        x = .5 * j
        y = .5 * (constant.ROWS - i)
        node.set_xy(x, y)
        empty_row.append(node)
      self.map.append(empty_row)

  def create_copy_of_map(self):
    ret = []
    for row in self.map:
      temp_row = []
      for node in row:
        temp_row.append(node)
      ret.append(temp_row)
    return ret


  def print_map_coords(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        print(f'({self.map[i][j].x},{self.map[i][j].y})', end="")
      print("")

  def print_obstacle_map(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        is_obstacle = 1 if self.map[i][j].is_obstacle else 0
        print(f'[ {is_obstacle} ]', end="")
      print("")

  # def print_start_and_goal_map(self):
  #   for i in range(constant.ROWS):
  #     for j in range(constant.COLS):
  #       temp = 1 if self.map[i][j].is_start or self.map[i][j].is_goal else 0
  #       print(f'[ {temp} ]', end="")
  #     print("")

  # def print_complete_map(self):
  #   for i in range(constant.ROWS):
  #     for j in range(constant.COLS):
  #       temp = ' '
  #       if(self.map[i][j].is_obstacle): temp = 'O'
  #       elif(self.map[i][j].is_start): temp = 'S'
  #       elif(self.map[i][j].is_goal): temp = 'G'
  #       print(f'[ {temp} ]', end="")
  #     print("")

  # def print_manhattan_map(self):
  #   for i in range(constant.ROWS):
  #     for j in range(constant.COLS):
  #       temp = self.map[i][j].man_val if self.map[i][j].man_val != None else ' '
  #       print(f'[ {temp} ]', end="")
  #     print("")

  def print_visited_map(self):
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        if(self.map[i][j].is_start): print(' O ', end="")
        elif(self.map[i][j].is_goal): print(' X ', end="")
        elif(self.map[i][j].visited): print(' - ', end="")
        else: print('   ', end="")
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
          elif(node.y == constant.ROWS/2)
            node.set_is_obstacle()
          elif(node.x == 0)
            node.set_is_obstacle()

  # def set_start_and_goal(self):
  #   self.start = ( round(constant.START[0] * constant.METERS_TO_FEET, 2), round(constant.START[1] * constant.METERS_TO_FEET, 2) )
  #   self.goal = ( round(constant.GOAL[0] * constant.METERS_TO_FEET, 2), round(constant.GOAL[1] * constant.METERS_TO_FEET, 2) )
  #   for row in self.map:
  #     for node in row:
  #       if((node.x, node.y) == self.start):
  #         node.set_is_start()
  #       elif((node.x, node.y) == self.goal):
  #         node.set_is_goal()

  def set_start_and_goal(self):
    self.start = ( round(constant.START[0] * constant.METERS_TO_FEET, 2), round(constant.START[1] * constant.METERS_TO_FEET, 2) )
    self.goal = ( round(constant.GOAL[0] * constant.METERS_TO_FEET, 2), round(constant.GOAL[1] * constant.METERS_TO_FEET, 2) )
    for i in range(constant.ROWS):
      for j in range(constant.COLS):
        node = self.map[i][j]
        if((node.x, node.y) == self.start):
          node.set_is_start()
          self.start_ij = (i, j) # TODO: can probably be deleted
          self.curr_ij = (i, j) # keep track of where we are on map
        elif((node.x, node.y) == self.goal):
          node.set_is_goal()
          self.goal_ij = (i, j) # used to check in our algorithm if it has been "visited" yet
  
  def set_man_values(self):
    for m in range(constant.ROWS * constant.COLS):
      #temp = copy.deepcopy(self.map)
      temp = self.create_copy_of_map()
      
      for i in range(constant.ROWS):
        for j in range(constant.COLS):
          if(self.map[i][j].man_val != None):
            continue

          if j+1 != constant.COLS and temp[i][j+1].man_val != None and temp[i][j+1].man_val != -1:
            self.map[i][j].man_val = temp[i][j+1].man_val + 1

          elif j-1 != -1 and temp[i][j-1].man_val != None and temp[i][j-1].man_val != -1:
            self.map[i][j].man_val = temp[i][j-1].man_val + 1

          elif i+1 != constant.ROWS and temp[i+1][j].man_val != None and temp[i+1][j].man_val != -1:
            self.map[i][j].man_val = temp[i+1][j].man_val + 1

          elif i-1 != -1 and temp[i-1][j].man_val != None and temp[i-1][j].man_val != -1:
            self.map[i][j].man_val = temp[i-1][j].man_val + 1

  def visited_goal(self):
    i, j = self.goal_ij
    return self.map[i][j].visited

  def get_neighbors(self):
    i, j = self.curr_ij

    ## each neighbor in the list will look like (i, j, neighboring_node)
    neighbors = []  

    ## If statements make sure we do not grab out of bounds or an obstacle
    if(j + 1 != constant.COLS and not self.map[i][j+1].is_obstacle):
      neighbors.append((i, j+1, self.map[i][j+1]))

    if(i + 1 != constant.ROWS and not self.map[i+1][j].is_obstacle):
      neighbors.append((i+1, j, self.map[i+1][j]))

    if(j - 1 != -1 and not self.map[i][j-1].is_obstacle):
      neighbors.append((i, j-1, self.map[i][j-1]))

    if(i - 1 != -1 and not self.map[i-1][j].is_obstacle):
      neighbors.append((i-1, j, self.map[i-1][j]))

    return neighbors

  def get_turning_commands(self, desired_dir):
    if(self.curr_dir == desired_dir):
      return []
    elif( (self.curr_dir == constant.EAST and desired_dir == constant.SOUTH) or 
          (self.curr_dir == constant.SOUTH and desired_dir == constant.WEST) or 
          (self.curr_dir == constant.WEST and desired_dir == constant.NORTH) or 
          (self.curr_dir == constant.NORTH and desired_dir == constant.EAST) ):
      return ['turn_right']
    elif( (self.curr_dir == constant.EAST and desired_dir == constant.NORTH) or 
          (self.curr_dir == constant.SOUTH and desired_dir == constant.EAST) or 
          (self.curr_dir == constant.WEST and desired_dir == constant.SOUTH) or 
          (self.curr_dir == constant.NORTH and desired_dir == constant.WEST) ):
      return ['turn_left']
    else:
      return ['turn_right', 'turn_right']

  def next_node(self):
    neighbors = self.get_neighbors()
    min_ij = neighbors[0][0], neighbors[0][1] ## default neighbor to go to
    min_man_val = neighbors[0][2].man_val ## default shortest distance neighbor

    for neighbor in neighbors:
      if neighbor[2].man_val < min_man_val:
        min_ij = neighbor[0], neighbor[1]
        min_man_val = neighbor[2].man_val

    i, j = self.curr_ij ## where robot currently is
    next_direction = constant.EAST ## assume we are going to move east / (right)
    if((i+1, j) == min_ij):
      next_direction = constant.SOUTH
    elif((i, j-1) == min_ij):
      next_direction = constant.WEST
    elif((i-1, j) == min_ij):
      next_direction = constant.NORTH

    turning_commands = self.get_turning_commands(next_direction)
    full_commands = turning_commands + ['move']

    ## set "current" vals to the node we are moving to
    self.curr_ij = min_ij
    self.curr_dir = next_direction
    i, j = self.curr_ij
    self.map[i][j].visited = True

    return full_commands


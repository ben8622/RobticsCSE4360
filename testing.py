import Classes
import constant

map = Classes.Map()
map.set_obstacles()
map.set_start_and_goal()
map.set_man_values()
# map.print_map()
# map.print_obstacle_map()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# map.print_map_coords()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# map.print_start_and_goal_map()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#map.print_complete_map()

#map.print_manhattan_map()
# map.print_obstacle_map()

#while(!map.visited_goal()):
while(not map.visited_goal()):
  commands = map.next_node()
  print(commands)
map.print_visited_map()
map.print_map_coords()
print(constant.ROWS/2)
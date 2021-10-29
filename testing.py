import Classes

map = Classes.Map()
# map.print_map()
map.set_obstacles()
map.set_start_and_goal()
# map.print_obstacle_map()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# map.print_map_coords()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# map.print_start_and_goal_map()
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#map.print_complete_map()
map.set_man_values()

map.print_manhattan_map()
# map.print_obstacle_map()
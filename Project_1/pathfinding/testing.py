import Classes
import constant

## init Map
map = Classes.Map()
map.set_obstacles()
map.set_start_and_goal()
map.set_man_values()

## Display complete map (shows obstacles, start, and goal)
map.print_complete_map()

## Do the "local" path finding
while(not map.visited_goal()):
  commands = map.next_node()

## Print nodes that have been visited
map.print_visited_map()
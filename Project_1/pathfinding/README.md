# Project 1 Pathfinding
Please refer to the writeup for a more detailed description of our solution to the pathfinding.

## Important Files
- `main.py` is the python code that will _actually_ run on the robot
- `test.py` is a playground used to test and run on your development machine, can be disregarded unless you want to see the output of printing functions and test without using the bot
- `constant.py` holds all of our constants throughout the project, please note than any speed/time constants work with OUR robot but you will have find out your own
- `Classes.py` contains our classes used in the project `Map` and `Node`
- `ProjectWriteUp.pdf` the main deliverable of the project with details on our software choices, hardware choices, and the path finding algorithm

## Running on the robot
The code that runs on the robot is the `main.py` file. Because this is using **micropython** you must make sure any print statements (in the main file or the classes used) are commented out. To download and run to the bot, please follow the [official Lego tutorial here](https://pybricks.com/ev3-micropython/startinstall.html)

## Running tests
There are many additional functions created in the **Map** class to help with debugging your code. Most of these are functions to print out the state of the map after. For example there is `print_visited_map()` which prints out the map and nodes that have been visited.

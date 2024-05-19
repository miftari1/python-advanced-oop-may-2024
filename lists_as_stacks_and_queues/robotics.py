from datetime import datetime, timedelta
from collections import deque
# Store the names of the robots from the input and their processing time in a list
robot_info = input().split(';')
# Create a dictionary
robots = {}
# Create a queue to store the products
products = deque()
# Store the name of the robot as a key, and as it's value the processing time and the remaining time when occupied
for robot in robot_info:
    robots[robot.split('-')[0]] = [int(robot.split('-')[1]), 0]
# Store the starting time in a variable using the strftime module
starting_time = datetime.strptime(input(), f'%H:%M:%S')
# Initialize a while loop until end command
while True:
    command = input()
    if command == 'End':
        break
    # for each iteration receive a products name and append it to the deque
    products.append(command)
# Create a while loop until there is products in the deque
while products:
    # for each iteration increase the starting time with 1 second
    starting_time += timedelta(0, 1)
    # pop the first product in the line
    current_product = products.popleft()
    # create a list to store the free robots
    free_robots = deque()
    # for each iteration check if there is a free robots
    for robot, value in robots.items():
        if value[1] != 0:
            value[1] -= 1
        else:
            free_robots.append([robot, value])
            continue
    if not free_robots:
        products.append(current_product)
    else:
        robots[free_robots[0][0]][1] = free_robots[0][1][0] - 1
        print(f'{free_robots[0][0]} - {current_product} [{starting_time.time()}]')
        free_robots.popleft()



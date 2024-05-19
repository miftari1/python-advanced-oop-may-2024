from datetime import datetime,timedelta
from collections import deque


def dictionary_build():
    """Creates a dictionary, with each robot's name and a list with it's processing time and it's index,\
    then adds it to a list."""
    for robot_info in robots_list:
        name, processing_time = robot_info.split('-')
        assembly_line[name] = []
        assembly_line[name].append(int(processing_time))
        assembly_line[name].append('is_available')
        assembly_line[name].append(0)


def add_to_queue(prod):
    """Adds a product to the queue."""
    products_queue.append(prod)


# Split the given list and add each element to a dictionary
robots_list = input().split(';')
assembly_line = dict()

dictionary_build()

current_time = datetime.strptime(input(), '%H:%M:%S')
tdelta = timedelta(seconds=1)
products_queue = deque()

# Adds a product to the queue until receives an 'End' command
product = input()
while product != 'End':
    add_to_queue(product)
    product = input()

# Iterates while there are elements in the queue
while products_queue:
    # Updates the current time with one second
    current_time += tdelta
    current_product = products_queue.popleft()

    # Iterates through the robots dict and checks if current time corresponds to the finish time of the product for
    # the robot and makes it available again
    for robot in assembly_line.keys():
        time_to_finish = assembly_line[robot][2]
        if current_time == time_to_finish:
            assembly_line[robot][1] = 'is_available'

    is_processed = False
    for robot in assembly_line.keys():
        indicator = assembly_line[robot][1]
        if indicator != 'is_available':
            continue
        else:
            print(f'{robot} - {current_product} [{current_time.time()}]')
            assembly_line[robot][1] = 'occupied'
            time_to_finish = current_time + timedelta(seconds=assembly_line[robot][0])
            assembly_line[robot][2] = time_to_finish
            is_processed = True
            break
    if not is_processed:
        products_queue.append(current_product)

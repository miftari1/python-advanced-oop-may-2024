from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_queue = deque()
crossroad = deque()
cars_passed = 0

while True:
    command = input()
    if command == 'End':
        break
    elif command == 'green':
        for i in range(green_light_duration):
            if not crossroad:
                current_car = cars_queue.popleft()
                crossroad.append(current_car.split())
            current_char = crossroad.popleft()
    else:
        cars_queue.append(command)
else:
    pass

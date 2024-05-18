from collections import deque


def add_car_to_queue(cmd, queue):
    """Adds given car to a deque."""
    queue.append(list(cmd))


def green_light(duration1, duration2, queue1, queue2):
    """Each car in the queue exits the crossroad one by one."""
    global crashed, cars_passed
    current_car = ''
    for i in range(duration1):
        if not queue2:
            try:
                current_car = queue1.popleft()
                queue2.extend(list(current_car))
            except IndexError:
                break
        queue2.popleft()
        if not queue2:
            cars_passed += 1

    if queue2:
        for i in range(duration2):
            queue2.popleft()
            if not queue2:
                cars_passed += 1
                break
        if queue2:
            character_hit = crossroad.popleft()
            crashed = True
            print(f'A crash happened! \n{"".join(current_car)} was hit at {character_hit}.')
            return


green_light_duration = int(input())
free_window_duration = int(input())

cars_queue = deque()
crossroad = deque()
cars_passed = 0
crashed = False

car = input()
while car != 'END':
    if car != 'green':
        add_car_to_queue(car, cars_queue)
    else:
        green_light(green_light_duration, free_window_duration, cars_queue, crossroad)
        if crashed:
            break
    car = input()
else:
    print(f'Everyone is safe. \n{cars_passed} total cars passed the crossroads.')

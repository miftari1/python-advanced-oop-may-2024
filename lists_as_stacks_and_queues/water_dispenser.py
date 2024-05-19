from collections import deque
available_water = int(input())
names_deque = deque()
while True:
    name = input()
    if name == "Start":
        break
    names_deque.append(name)
while True:
    command = input()
    if command == "End":
        break
    command_elements = command.split()
    if "refill" in command_elements:
        liters = int(command_elements[1])
        available_water += liters
    else:
        liters = int(command_elements[0])
        if available_water >= liters:
            available_water -= liters
            print(f"{names_deque.popleft()} got water")
        else:
            print(f"{names_deque.popleft()} must wait")
print(f"{available_water} liters left")
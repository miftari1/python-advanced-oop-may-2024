#import the deque library from collections library
from collections import deque
# create a dictionary to store the gas stations with their information
gas_stations_dict = {}

# create a secondary deque to store the gas stations which respond to the condition
stations_deque = deque()

# create a variable of type integer to store the correct answer
answer = 0

# create an integer variable to store the sum of the petrol
sum_of_petrol = 0

# create a counter to store the number of passed stations
station_counter = 0

# create a for loop to add each gas station to the dictionary
for station in range(int(input())):

    # add the station to the deque
    stations_deque.append(station)

    # add the station to the dictionary
    gas_stations_dict[station] = []

    # create a local variable of type list to store the amount of petrol and the distance to the next gas station
    information = input().split()

    # create a variable of type integer to store the first element in the list variable which is the amount of petrol
    current_fill = int(information[0])

    # create a second variable of type integer to store the the\
    # second element in the list variable which is the distance
    current_distance = int(information[1])

    # add the info to the each gas_station key
    gas_stations_dict[station].append(current_fill)
    gas_stations_dict[station].append(current_distance)

# initialize a while loop until the condition is not True
while station_counter != len(gas_stations_dict.keys()):

    # add the amount of petrol to the sum of petrol variable
    sum_of_petrol += gas_stations_dict[stations_deque[0]][0]

    # def function to check if there is enough petrol and return True if yes and False if no
    def petrol_check(petrol, distance):
        if petrol >= distance:
            return True
        else:
            return False

    # create a condition which checks if the amount of petrol available is higher or equal than the current distance
    if petrol_check(sum_of_petrol, gas_stations_dict[stations_deque[0]][1]):

        # increase the counter with 1 if true
        station_counter += 1
        sum_of_petrol -= gas_stations_dict[stations_deque[0]][1]

    # return the counter and the sum of petrol to zero if false
    else:
        station_counter = 0
        sum_of_petrol = 0

    # move the current station to the last index
    not_responding = stations_deque.popleft()
    stations_deque.append(not_responding)

# print the first element from the stations deque
print(stations_deque[0])


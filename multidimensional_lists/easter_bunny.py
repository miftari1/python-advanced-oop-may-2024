size = int(input())
trap = 'X'
matrix = []
bunny = []

directions = {
    'up': [-1, bunny[1]],
    'down': [size -1, bunny[1]],
    'left': [bunny[0], -1],
    'right': [bunny[0], size - 1]
}

for row in range(size):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny = [row, matrix[row].index('B')]

max_eggs = 0
max_eggs_positions = []
best_direction = ''
for direction, index_direction in directions.items():
    eggs = 0
    eggs_positions = []
    if direction == 'up':
        if bunny[0] - 1 >= 0:
            for row in range(bunny[0] - 1, -1, -1):
                current_position = matrix[row][bunny[1]]
                if current_position == trap:
                    break
                else:
                    if int(current_position) >= 0:
                        eggs += int(current_position)
                        eggs_positions.append([row, bunny[1]])
            if eggs >= max_eggs:
                max_eggs = eggs
                best_direction = direction
                max_eggs_positions = eggs_positions
    elif direction == 'down':
        if bunny[0] + 1 <= size - 1:
            for row in range(bunny[0] + 1, size):
                current_position = matrix[row][bunny[1]]
                if current_position == trap:
                    break
                else:
                    if int(current_position) >= 0:
                        eggs += int(current_position)
                        eggs_positions.append([row, bunny[1]])
            if eggs >= max_eggs:
                max_eggs = eggs
                best_direction = direction
                max_eggs_positions = eggs_positions
    elif direction == 'left':
        if bunny[1] - 1 >= 0:
            for col in range(bunny[1] - 1, -1, -1):
                current_position = matrix[bunny[0]][col]
                if current_position == trap:
                    break
                else:
                    if int(current_position) >= 0:
                        eggs += int(current_position)
                        eggs_positions.append([bunny[0], col])
            if eggs >= max_eggs:
                max_eggs = eggs
                best_direction = direction
                max_eggs_positions = eggs_positions
    else:
        if bunny[1] + 1 <= size - 1:
            for col in range(bunny[1] + 1, size):
                current_position = matrix[bunny[0]][col]
                if current_position == trap:
                    break
                else:
                    if int(current_position) >= 0:
                        eggs += int(current_position)
                        eggs_positions.append([bunny[0], col])
            if eggs >= max_eggs:
                max_eggs = eggs
                best_direction = direction
                max_eggs_positions = eggs_positions
print(best_direction)
for point in max_eggs_positions:
    print(point)
print(max_eggs)

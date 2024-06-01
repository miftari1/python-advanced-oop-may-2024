shotgun_range = []
my_position = []
targets_count = 0
targets_hit = 0
targets_positions = []

for row_number in range(5):
    current_row = input().split()
    if 'A' in current_row:
        my_position = [row_number, current_row.index('A')]
    if 'x' in current_row:
        targets_count += current_row.count('x')
    shotgun_range.append(current_row)

directions = {'up': [-1, 0],
              'down': [1, 0],
              'left': [0, -1],
              'right': [0, 1]
              }

num_commands = int(input())

is_completed = False

for _ in range(num_commands):
    command = input().split()
    direction = command[1]

    if 'move' in command:
        steps = int(command[2])
        for _ in range(steps):
            current_row, current_col = my_position[0], my_position[1]
            next_row = current_row + directions[direction][0]
            next_col = current_col + directions[direction][1]

            if 0 <= next_row < 5 and 0 <= next_col < 5:
                if shotgun_range[next_row][next_col] == 'x':
                    break
                else:
                    shotgun_range[current_row][current_col] = '.'
                    shotgun_range[next_row][next_col] = 'A'
                    my_position = [next_row, next_col]

    elif 'shoot' in command:
        bullet_row = my_position[0]
        bullet_col = my_position[1]
        while 0 <= bullet_row < 5 and 0 <= bullet_col < 5:
            if shotgun_range[bullet_row][bullet_col] == 'x':
                targets_hit += 1
                shotgun_range[bullet_row][bullet_col] = '.'
                targets_positions.append([bullet_row, bullet_col])
                if targets_hit == targets_count:
                    is_completed = True
                    print(f'Training completed! All {targets_count} targets hit.')
                break
            bullet_row += directions[direction][0]
            bullet_col += directions[direction][1]

    if is_completed:
        break
else:
    targets_left = targets_count - targets_hit
    print(f'Training not completed! {targets_left} targets left.')

if targets_positions:
    for row in targets_positions:
        print(row)

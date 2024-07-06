def move_bee(matrix, dir):
    global bee_position, next_symbol
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    row, col = bee_position[0], bee_position[1]
    next_row = row + directions[dir][0]
    next_col = col + directions[dir][1]
    if next_row < 0:
        next_row = len(matrix) - 1
    elif next_row == len(matrix):
        next_row = 0
    if next_col < 0:
        next_col = len(matrix) - 1
    elif next_col == len(matrix):
        next_col = 0

    matrix[row][col] = '-'
    next_symbol = matrix[next_row][next_col]
    matrix[next_row][next_col] = 'B'

    return [next_row, next_col]


field = []
bee_position = []

n = int(input())
for row_idx in range(n):
    current_row = list(input())
    if 'B' in current_row:
        col_idx = current_row.index('B')
        bee_position = [row_idx, col_idx]
    field.append(current_row)

collected_nectar = 0
bee_energy = 15
next_symbol = ''
restored_energy = 0

while bee_energy > 0:
    command = input()
    bee_position = move_bee(field, command)
    bee_energy -= 1
    if next_symbol == 'H':
        if collected_nectar >= 30:
            print(f'Great job, Beesy! The hive is full. Energy left: {bee_energy}')
        elif collected_nectar < 30:
            print(f'Beesy did not manage to collect enough nectar.')
        break
    elif next_symbol != '-':
        collected_nectar += int(next_symbol)
    if bee_energy == 0:
        if collected_nectar >= 30 and restored_energy < 1:
            bee_energy = collected_nectar - 30
            restored_energy += 1
else:
    print(f'This is the end! Beesy ran out of energy.')

for row in field:
    print(''.join(row))

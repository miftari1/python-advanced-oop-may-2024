size = int(input())

wonderland_map = []
alice_position = []

for row in range(size):
    current_row = input().split()
    if 'A' in current_row:
        alice_position = [row, current_row.index('A')]
    wonderland_map.append(current_row)

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

is_end = False
bags_tea = 0
while bags_tea < 10:
    command = input()
    for direction, indices in directions.items():
        if command == direction:
            current_row = alice_position[0]
            current_col = alice_position[1]
            next_row = current_row + indices[0]
            next_col = current_col + indices[1]
            if 0 > next_row or next_row == size or 0 > next_col or next_col == size:
                wonderland_map[current_row][current_col] = '*'
                is_end = True
                break
            elif wonderland_map[next_row][next_col] == 'R':
                wonderland_map[current_row][current_col] = '*'
                wonderland_map[next_row][next_col] = '*'
                is_end = True
                break
            else:
                if wonderland_map[next_row][next_col] != '*' and wonderland_map[next_row][next_col] != '.':
                    bags_tea += int(wonderland_map[next_row][next_col])
                wonderland_map[current_row][current_col] = '*'
                alice_position = [next_row, next_col]
    if is_end:
        break

else:
    wonderland_map[alice_position[0]][alice_position[1]] = '*'
    print(f'She did it! She went to the party.')

if is_end:
    print('Alice didn\'t make it to the tea party.')

for row in wonderland_map:
    print(*row, sep=' ')

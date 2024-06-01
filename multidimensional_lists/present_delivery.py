def move_santa(td_list, nrow, ncol, position):
    row = position[0]
    col = position[1]
    td_list[row][col] = '-'
    td_list[nrow][ncol] = 'S'
    return [nrow, ncol]


def check_presents(num_presents):
    if num_presents == 0:
        return True


count_presents = int(input())
size = int(input())
neighborhood = []
santa_position = []
nice_kids = 0
kids_with_presents = 0

for row in range(size):
    current_row = input().split()
    if 'S' in current_row:
        santa_position = [row, current_row.index('S')]
    if 'V' in current_row:
        nice_kids += current_row.count('V')
    neighborhood.append(current_row)

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

command = input()
while command != 'Christmas morning':
    row = santa_position[0]
    col = santa_position[1]
    next_row = row + directions[command][0]
    next_col = col + directions[command][1]
    current_position_mark = neighborhood[next_row][next_col]

    if 0 <= next_row < size and 0 <= next_col < size:
        santa_position = move_santa(neighborhood, next_row, next_col, santa_position)

        if current_position_mark == 'C':
            crow = santa_position[0]
            ccol = santa_position[1]
            for values in directions.values():
                nrow = crow + values[0]
                ncol = ccol + values[1]
                if neighborhood[nrow][ncol] == 'V':
                    kids_with_presents += 1
                if neighborhood[nrow][ncol] != '-':
                    count_presents -= 1
                neighborhood[nrow][ncol] = '-'
                if check_presents(count_presents):
                    break

        elif current_position_mark == 'V':
            kids_with_presents += 1
            count_presents -= 1

        if check_presents(count_presents):
            kids_left = nice_kids - kids_with_presents
            if kids_left > 0:
                print(f'Santa ran out of presents!')
            break

    command = input()

for row in neighborhood:
    print(*row, sep=' ')

kids_left = nice_kids - kids_with_presents
if kids_left == 0:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
elif check_presents(count_presents) and kids_left > 0:
    print(f'No presents for {kids_left} nice kid/s.')

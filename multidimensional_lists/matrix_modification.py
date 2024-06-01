def add_number(cmd, td_list):
    row, col, value = int(cmd[1]), int(cmd[2]), int(cmd[3])
    if 0 <= row < len(td_list) and 0 <= col < len(td_list):
        td_list[row][col] += value
        return
    print(f'Invalid coordinates')
    return


def subtract_number(cmd, td_list):
    row, col, value = int(cmd[1]), int(cmd[2]), int(cmd[3])
    if 0 <= row < len(td_list) and 0 <= col < len(td_list):
        td_list[row][col] -= value
        return
    print(f'Invalid coordinates')
    return


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

command = input().split()
while 'END' not in command:

    if 'Add' in command:
        add_number(command, matrix)

    elif 'Subtract' in command:
        subtract_number(command, matrix)

    command = input().split()
else:
    for row in matrix:
        print(*row, sep=' ')

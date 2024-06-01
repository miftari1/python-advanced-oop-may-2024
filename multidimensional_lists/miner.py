from collections import deque


def move_up(row):
    """Decreases row index with 1 if in range"""
    if row - 1 < 0:
        return 0
    return 1


def move_down(matrix_size, row):
    """Increases row index with 1 if in range"""
    if row + 1 == matrix_size:
        return 0
    return 1


def move_left(col):
    """Decreases column index with 1 if in range"""
    if col - 1 < 0:
        return 0
    return 1


def move_right(matrix_size, col):
    """Increases column index with 1 if in range"""
    if col + 1 == matrix_size:
        return 0
    return 1


def count_coal(td_list):
    """Counts the quantity of coal in the matrix"""
    coal_count = 0
    for row in td_list:
        coal_count += row.count('c')
    return coal_count


def collect_coal(td_list, row, col):
    """Collects coal and changes current character with '*'"""
    td_list[row][col] = '*'
    return 1


def find_miner_position(td_list):
    """Search for the miner's position and returns it."""
    for row in range(len(td_list)):
        if 's' in td_list[row]:
            return [row, td_list[row].index('s')]


size = int(input())
commands = deque(input().split())
matrix = [input().split() for _ in range(size)]

found_all_coal = False
step_at_e = False

available_coal = count_coal(matrix)
row_index, col_index = find_miner_position(matrix)

while commands:
    current_command = commands.popleft()

    if current_command == 'left':
        col_index -= move_left(col_index)

    elif current_command == 'right':
        col_index += move_right(size, col_index)

    elif current_command == 'up':
        row_index -= move_up(row_index)

    elif current_command == 'down':
        row_index += move_down(size, row_index)

    if matrix[row_index][col_index] == 'c':
        available_coal -= collect_coal(matrix, row_index, col_index)
        if available_coal == 0:
            found_all_coal = True
            break

    if matrix[row_index][col_index] == 'e':
        step_at_e = True
        break
else:
    print(f'{available_coal} pieces of coal left. ({row_index}, {col_index})')

if found_all_coal:
    print(f'You collected all coal! ({row_index}, {col_index})')
if step_at_e:
    print(f'Game over! ({row_index}, {col_index})')

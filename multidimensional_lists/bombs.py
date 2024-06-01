from collections import deque
matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
bombs_coordinates = deque(input().split())

start_row = 0
end_row = 0
start_col = 0
end_col = 0

while bombs_coordinates:
    current_bomb_coordinates = list(map(int, bombs_coordinates.popleft().split(',')))
    bomb_row = current_bomb_coordinates[0]
    bomb_col = current_bomb_coordinates[1]
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value <= 0:
        continue
    matrix[bomb_row][bomb_col] = 0

    start_row = bomb_row - 1
    end_row = bomb_row + 1
    start_col = bomb_col - 1
    end_col = bomb_col + 1

    if bomb_row == 0:
        start_row = 0
    if bomb_row == matrix_size - 1:
        end_row = bomb_row

    if bomb_col == 0:
        start_col = 0
    if bomb_col == matrix_size - 1:
        end_col = bomb_col

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if matrix[row][col] > 0:
                matrix[row][col] -= bomb_value

alive_cells = []
for row in range(matrix_size):
    for col in range(matrix_size):
        current_digit = matrix[row][col]
        if current_digit > 0:
            alive_cells.append(current_digit)

num_alive_cells = len(alive_cells)
sum_alive_cells = sum(alive_cells)

print(f'Alive cells: {num_alive_cells}')
print(f'Sum: {sum_alive_cells}')

for row in matrix:
    print(*row, sep=' ')


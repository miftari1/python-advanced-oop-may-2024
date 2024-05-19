rows, columns = map(int, input().split(', '))
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]

max_sum = 0
found_submatrix = []
for row_index in range(rows - 1):
    current_row = matrix[row_index]
    second_row = matrix[row_index + 1]
    for column_index in range(columns - 1):
        current_submatrix = [current_row[column_index:column_index + 2], second_row[column_index:column_index + 2]]
        submatrix_sum = sum(current_submatrix[0]) + sum(current_submatrix[1])
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            found_submatrix = current_submatrix
for row in found_submatrix:
    print(*row, sep=' ')
print(max_sum)


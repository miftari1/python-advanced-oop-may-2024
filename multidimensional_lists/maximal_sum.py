max_sum = 0
max_value_submatrix = ''
rows, columns = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
for row in range(rows - 2):
    for column in range(columns - 2):
        submatrix = [matrix[sub_row + row][column:column + 3] for sub_row in range(3)]
        current_sum = 0
        for lst in submatrix:
            current_sum += sum(map(int, lst))
            if current_sum >= max_sum:
                max_sum = current_sum
                max_value_submatrix = submatrix
print(f'Sum = {max_sum}')
for lst in max_value_submatrix:
    print(' '.join(lst))


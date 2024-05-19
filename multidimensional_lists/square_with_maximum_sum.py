rows, columns = map(int, input().split(', '))
matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]
found_submatrix = ''
max_sum = 0
for row in range(rows - 1):
    for col in range(columns - 1):
        current_submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
        submatrix_sum = 0
        for element in current_submatrix:
            submatrix_sum += sum(element)
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            found_submatrix = current_submatrix
for element in found_submatrix:
    print(*element, sep=' ')
print(max_sum)


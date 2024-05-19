rows, columns = map(int, input().split(', '))
matrix = [[int(num) for num in input().split()] for _ in range(rows)]
for column in range(columns):
    sum_columns = 0
    for row in range(rows):
        sum_columns += matrix[row][column]
    print(sum_columns)
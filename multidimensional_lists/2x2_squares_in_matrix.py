identical_squares = 0
rows, columns = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
for row in range(rows - 1):
    for column in range(columns - 1):
        current_square = set()
        current_square.add(matrix[row][column])
        current_square.add(matrix[row][column + 1])
        current_square.add(matrix[row + 1][column])
        current_square.add(matrix[row + 1][column + 1])
        if len(current_square) == 1:
            identical_squares += 1
print(identical_squares)
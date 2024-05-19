rows = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(rows)]
diagonal_sum = 0
for row in range(rows):
    diagonal_sum += matrix[row][row]
print(diagonal_sum)
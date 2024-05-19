def find_diagonal_sum(size):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for row in range(size):
        current_row = input().split()
        primary_diagonal_sum += int(current_row[row])
        secondary_diagonal_sum += int(current_row[(len(current_row) - 1) - row])
    diagonal_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    return diagonal_difference


matrix_size = int(input())
print(find_diagonal_sum(matrix_size))



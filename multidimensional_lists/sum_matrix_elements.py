# read two numbers as a list and assign them to the rows and columns variables
rows, columns = map(int, input().split(', '))
# create an integer variable to store the sum of the matrix
matrix_sum = 0
# create a matrix using a comprehension
matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]
# start a for loop within the elements of the matrix and store the sum of them in the variable
for element in matrix:
    matrix_sum += sum(element)
# output the sum of the matrix
print(matrix_sum)
# output the matrix
print(matrix)


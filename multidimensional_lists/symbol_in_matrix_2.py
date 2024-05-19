matrix_lenght = int(input())
matrix = [input() for i in range(matrix_lenght)]
symbol_to_find = input()
for current_row in matrix:
    index = current_row.find(symbol_to_find)
    if index == -1:
        continue
    else:
        print(f'({matrix.index(current_row)}, {index})')
        break
else:
    print(f'{symbol_to_find} does not occur in the matrix')

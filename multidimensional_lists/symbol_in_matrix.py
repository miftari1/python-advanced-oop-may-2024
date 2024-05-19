rows = int(input())
matrix = [list(input()) for _ in range(rows)]
char_to_search = input()
for i in range(len(matrix)):
    if char_to_search in matrix[i]:
        print(f'({i}, {matrix[i].index(char_to_search)})')
        break
else:
    print(f'{char_to_search} does not occur in the matrix')
diagonals = {}


def create_matrix(number):
    matrix = [input().split(', ') for _ in range(number)]
    return matrix


def find_diagonals(matrix):
    diagonals['Primary diagonal'] = []
    diagonals['Secondary diagonal'] = []
    for row in range(len(matrix)):
        diagonals['Primary diagonal'].append(matrix[row][row])
        diagonals['Secondary diagonal'].append(matrix[row][(len(matrix) - 1) - row])
    for diagonal in diagonals.keys():
        print(f'{diagonal}: {", ".join(diagonals[diagonal])}. Sum: {sum(map(int, diagonals[diagonal]))}')


matrix_size = int(input())
find_diagonals(create_matrix(matrix_size))
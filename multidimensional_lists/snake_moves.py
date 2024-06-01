from collections import deque


def snake_moves(r, c, text):
    matrix = []
    i = 0

    for row in range(1, r + 1):
        if row % 2 == 0:
            matrix.append(deque())
            for column in range(c):
                current_letter = text[i]
                matrix[row - 1].appendleft(current_letter)
                i += 1
                if i == len(text):
                    i = 0
        else:
            matrix.append(list())
            for column in range(c):
                current_letter = text[i]
                matrix[row - 1].append(current_letter)
                i += 1
                if i == len(text):
                    i = 0

    return matrix


rows, columns = map(int, input().split())

snake = input()

td_list = snake_moves(rows, columns, snake)

for row in td_list:
    print(''.join(row))


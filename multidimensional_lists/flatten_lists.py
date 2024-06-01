matrix = [element.split() for element in input().split('|')]
for row in reversed(matrix):
    if row:
        print(' '.join(row), end=' ')

size = int(input())
chess_board = []
knights = []
moves = [(2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1),  (-1, -2)]
max_attacks = 0
no_attacks = False
for row in range(size):
    chess_board.append(list(input()))
    for col in range(size):
        if chess_board[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0
while True:
    max_attacks = 0
    max_knight = []
    for knight in knights:
        attacks = 0
        for move in moves:
            next_row = knight[0] + move[0]
            next_col = knight[1] + move[1]
            if 0 <= next_row < size and 0 <= next_col < size:
                if chess_board[next_row][next_col] == 'K':
                    attacks += 1
        if attacks > max_attacks:
            max_attacks = attacks
            max_knight = knight
    if max_attacks == 0:
        print(removed_knights)
        break
    chess_board[max_knight[0]][max_knight[1]] = '0'
    knights.remove(max_knight)
    removed_knights += 1



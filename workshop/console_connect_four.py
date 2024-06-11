def create_matrice():
    matrix = []
    for _ in range(ROWS):
        lst = []
        for _ in range(COLS):
            lst.append(0)
        matrix.append(lst)
    return matrix


def pick_a_field(name, symb):
    print(f'{name}, please choose a column')
    try:
        chosen_column = int(input()) - 1
        if chosen_column in free_positions:
            available_row = free_positions[chosen_column]
            board[available_row][chosen_column] = symb
            free_positions[chosen_column] -= 1
            if free_positions[chosen_column] < 0:
                del free_positions[chosen_column]
            return [available_row, chosen_column, symb]
        else:
            return 0
    except ValueError:
        print('Please provide valid number.')
        return 0


def show_board(matrix):
    for row in matrix:
        print(row)


def check_for_winner(position, matrix, symb):
    global got_winner

    row = position[0]
    col = position[1]
    positions_to_check = {
        'up': [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
        'down': [(0, 0), (1, 0), (2, 0), (3, 0)],
        'left': [(0, 0), (0, -1), (0, -2), (0, -3)],
        'right': [(0, 0), (0, 1), (0, 2), (0, 3)],
        'up-left': [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
        'up-right': [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
        'down-left': [(0, 0), (1, -1), (2, -2), (3, -3)],
        'down-right': [(0, 0), (1, 1), (2, 2), (3, 3)]
    }
    for position in positions_to_check.keys():
        consecutive_fields = []
        for indexes in positions_to_check[position]:
            current_row = row + indexes[0]
            current_col = col + indexes[1]
            if 0 <= current_row < ROWS and 0 <= current_col < COLS:
                consecutive_fields.append(matrix[current_row][current_col])
        if consecutive_fields == [symb, symb, symb, symb]:
            print(f'The winner is Player{symb}')
            got_winner = True
            return


# Main game block
got_winner = False
ROWS = 6
COLS = 7
free_positions = {}

board = create_matrice()
# Creates a dictionary of the free positions in the matrix
for col in range(COLS):
    free_positions[col] = 5

turn = 1
while not got_winner:
    if turn % 2 != 0:
        result = pick_a_field('Player1', 1)
    else:
        result = pick_a_field('Player2', 2)
    show_board(board)

    if result == 0:
        print('Please provide a correct column')
        turn += 2
        continue

    check_for_winner(result, board, result[2])
    turn += 1

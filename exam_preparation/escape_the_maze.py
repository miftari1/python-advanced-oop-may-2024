from collections import deque


def escape_the_maze(size):

    monster_defeat = False
    escaped = False
    player_position = []
    maze = []
    health = 100

    directions = {
        'up': [-1, 0],
        'down': [1, 0],
        'left': [0, -1],
        'right': [0, 1]
    }

    # Reading the matrice
    for row_index in range(size):
        row = list(input())
        if 'P' in row:
            # Assign player's initial position to a variable
            player_position = [row_index, row.index('P')]
        maze.append(row)
    # Until certain condition
    while True:
        command = input()
        current_row, current_col = player_position[0], player_position[1]
        next_row = current_row + directions[command][0]
        next_col = current_col + directions[command][1]

        # Check if next step is valid
        if 0 <= next_row < size and 0 <= next_col < size:
            next_step_char = maze[next_row][next_col]

            # Move accordingly to the current command
            maze[current_row][current_col] = '-'
            maze[next_row][next_col] = 'P'
            player_position = [next_row, next_col] # Sets the next step as current

            if next_step_char == 'M':
                health -= 40
                if health <= 0: # Game over
                    health = 0
                    monster_defeat = True
                    break
            elif next_step_char == 'H':
                health += 15
                if health > 100:
                    health = 100
            elif next_step_char == 'X':
                escaped = True
                break

    if monster_defeat:
        print('Player is dead. Maze over!')
    elif escaped:
        print('Player escaped the maze. Danger passed!')

    print(f'Player\'s health: {health} units')

    for row in maze:
        print(''.join(row))


matrice_size = int(input())
escape_the_maze(matrice_size)
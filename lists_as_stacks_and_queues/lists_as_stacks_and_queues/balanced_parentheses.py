from collections import deque
# create a list variable as a deque to store the parenthesis given from the user
sequence = deque(input())

# create a variable of type list to store the open parenthesis
open_parenthesis = []

# create a while loop to iterate through the deque until there is elements
while sequence:
    left_parentheses = sequence.popleft()
    # create a nested if condition to verify if the current parenthesis is opening
    if left_parentheses in '({[':

        # add the element in the list and delete it from the deque if true
        open_parenthesis.append(left_parentheses)

    # create a nested elif statement to break the program if the list is empty and the parenthesis is not an\
    # opening and output 'No' as an answer
    elif not open_parenthesis:
        print('NO')
        break
    # create a nested elif statement to check if the combination between the first opening\
    # and the current closing brackets is valid
    elif f'{open_parenthesis.pop() + left_parentheses}' not in '{}[]()':
        print('NO')
        break


# create an else statement which outputs 'Yes' as an answer
else:
    print('YES')
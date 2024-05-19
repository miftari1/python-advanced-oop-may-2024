# Read a text and create a tuple
user_input = tuple(input('Write something here:'))
# Read a integer number for step
step = int(input('Step:'))
# Check if the tuple is empty
if not user_input:
    # If yes, output information that the tuple is empty
    print('You need to write something')
# Else generate a new tuple, based on the previous and add each element with the given step
else:
    new_tuple = tuple(user_input[i] for i in range(0, len(user_input), step))
    # Output the new tuple
    print(new_tuple)
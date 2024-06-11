from collections import deque
# Read a sequence of integers separated by comma representing bowls of ramen and store them as a stack.
# Convert the values to integer
bowls = list(map(int, input().split(', ')))
# Read a sequence of integers separated by comma representing the customers and store them as a queue
customers = deque(map(int, input().split(', ')))
# Initialize a while loop until there are customers in the queue
while customers:
    # Check whether the current customer's value or the current bowls of ramen are greater
    # Lower the greater value with the smaller and delete the last from it's list
    if customers[0] > bowls[-1]:
        customers[0] -= bowls[-1]
        bowls.pop()
    elif customers[0] < bowls[-1]:
        bowls[-1] -= customers[0]
        customers.popleft()
    # If both values are equal, delete them both
    else:
        customers.popleft()
        bowls.pop()
    # Check if there is bowls in the stack
    # Break the loop if not and print the customers left in the needed format
    if not bowls and customers:
        left_customers = ', '.join(map(str, customers))
        print(f'Out of ramen! You didn\'t manage to serve all customers.')
        print(f'Customers left: {left_customers}')
        break
    elif not bowls and not customers:
        print('Great job! You served all the customers.')
        break
# If the loop finishes successfully print the bowls of ramen left in the needed format
else:
    left_bowls = ', '.join(map(str, bowls))
    print(f'Great job! You served all the customers.')
    if bowls:
        print(f'Bowls of ramen left: {left_bowls}')

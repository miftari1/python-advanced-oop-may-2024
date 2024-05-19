from collections import deque
food_quantity = int(input())
orders_sequence = deque([int(order) for order in input().split()])
print(max(orders_sequence))
while orders_sequence:
    if food_quantity >= orders_sequence[0]:
        current_order = orders_sequence.popleft()
        food_quantity -= current_order
    else:
        break
if not orders_sequence:
    print(f'Orders complete')
else:
    orders_left = ' '.join(map(str, orders_sequence))
    print(f'Orders left: {orders_left}')
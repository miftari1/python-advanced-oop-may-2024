from collections import deque
customers_deque = deque()
while True:
    customer_name = input()
    if customer_name == "Paid":
        while customers_deque:
            print(customers_deque.popleft())
    elif customer_name == "End":
        print(f"{len(customers_deque)} people remaining.")
        break
    else:
        customers_deque.append(customer_name)
from collections import deque
kids_names = deque(input().split())
toss_number = int(input())
counter = 0
while len(kids_names) > 1:
    counter += 1
    removed_kid = kids_names.popleft()
    if counter != toss_number:
        kids_names.append(removed_kid)
    else:
        print(f"Removed {removed_kid}")
        counter = 0
print(f"Last is {kids_names[0]}")
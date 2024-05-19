from collections import deque
cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    if current_bottle >= current_cup:
        wasted_water += (current_bottle - current_cup)
    else:
        current_cup -= current_bottle
        while current_cup > 0:
            current_bottle = bottles.pop()
            if current_bottle >= current_cup:
                wasted_water += (current_bottle - current_cup)
            current_cup -= current_bottle
            if not bottles:
                break

    if not bottles:
        break

else:
    print('Bottles:', end=' ')
    for bottle in bottles:
        print(f'{bottle}', end=' ')

if cups:
    print('Cups:', end=' ')
    for cup in cups:
        print(f'{cup}', end=' ')

print(f'\nWasted litters of water: {wasted_water}')

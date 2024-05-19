from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

bullets_fired = 0
while locks:
    bullets_fired += 1

    current_bullet = bullets.pop()
    if current_bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

    if bullets_fired % gun_barrel_size == 0:
        if bullets:
            print('Reloading!')
    if not bullets and locks:
        print(f'Couldn\'t get through. Locks left: {len(locks)}')
        break

else:
    money_earned = intelligence_value - bullets_fired * bullet_price
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')

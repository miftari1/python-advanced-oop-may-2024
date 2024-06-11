from collections import deque


def pie_pursuit(contestants, pies):
    while contestants and pies:
        current_contestant = contestants.popleft()
        current_pie = pies.pop()

        if current_contestant >= current_pie:
            current_contestant -= current_pie
            if current_contestant > 0:
                contestants.append(current_contestant)

        else:
            current_pie -= current_contestant
            if pies and current_pie == 1:
                pies[-1] += current_pie
                continue
            pies.append(current_pie)

    if not contestants and not pies:
        return 'We have a champion!'
    elif contestants:
        return f'We will have to wait for more pies to be baked!\nContestants left: {", ".join(map(str, contestants))}'
    elif pies:
        return f'Our contestants need to rest!\nPies left: {", ".join(map(str, pies))}'


contestants_capacity = deque(map(int, input().split()))
pies_sizes = list(map(int, input().split()))
print(pie_pursuit(contestants_capacity, pies_sizes))

rows = int(input())
lst = []
for _ in range(rows):
    lst.extend(map(int, input().split(', ')))
print(lst)
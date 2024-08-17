def fibonacci():
    previous, current = 0, 1
    while True:
        yield previous
        previous, current = current, current + previous


generator = fibonacci()
for i in range(10):
    print(next(generator))
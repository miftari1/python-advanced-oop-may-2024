def sorting_cheeses(**kwargs):
    result = dict(sorted(kwargs.items(), key=lambda x: x[0]))
    for key, value in result.items():
        value.sort(reverse=True)
        print(f'{key}')
        for num in value:
            print(num)




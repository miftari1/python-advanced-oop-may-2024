def even_odd_filter(**kwargs):
    filtered_lists = {}

    for command, nums_lst in kwargs.items():
        if command == 'even':
            even_lst = [num for num in nums_lst if num % 2 == 0]
            filtered_lists[command] = even_lst
        else:
            odd_lst = [num for num in nums_lst if num % 2 != 0]
            filtered_lists[command] = odd_lst

    filtered = dict(sorted(filtered_lists.items(), key=lambda item: len(item[1]), reverse=True))

    return filtered


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))

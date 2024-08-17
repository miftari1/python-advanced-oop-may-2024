from itertools import permutations


def possible_permutations(lst_of_nums):
    if len(lst_of_nums) <= 1:
        yield lst_of_nums
    for permutation in permutations(lst_of_nums):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
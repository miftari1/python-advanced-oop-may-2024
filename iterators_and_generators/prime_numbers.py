from typing import List


def get_primes(seq: List[int]):
    for num in seq:
        if num > 1:
            for divisor in range(2, num):
                if num % divisor == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
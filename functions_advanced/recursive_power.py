def recursive_power(number, power):
    if power == 0:
        return 1
    elif power == 1:
        return number
    else:
        return number * recursive_power(number, power - 1)

def operate(operator, *numbers):
    global result
    if operator == '+':
        result = 0
        for num in numbers:
            result += num

    elif operator == '-':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num

    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num

    elif operator == '/':
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    return result

def even_parameters(function):
    def wrapper(*numbers):
        for num in numbers:
            if not isinstance(num, int) or num % 2 != 0:
                return 'Please use only even numbers!'
        result = function(*numbers)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
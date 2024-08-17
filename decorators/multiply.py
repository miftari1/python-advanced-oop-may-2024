def multiply(multiply_by):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            product = result * multiply_by
            return product
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
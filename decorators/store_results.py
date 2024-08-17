class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        info = f'Function {self.func.__name__} was called. Result: {self.func(*args)}'
        with open('results.txt', 'a') as file:
            file.write(f'{info}\n')


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)

mult(6, 4)
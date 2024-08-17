def make_bold(func):
    def wrapper(*args):
        txt = func(*args)
        return f'<b>{txt}</b>'
    return wrapper


def make_italic(func):
    def wrapper(*args):
        txt = func(*args)
        return f'<i>{txt}</i>'
    return wrapper


def make_underline(func):
    def wrapper(*args):
        txt = func(*args)
        return f'<u>{txt}</u>'
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
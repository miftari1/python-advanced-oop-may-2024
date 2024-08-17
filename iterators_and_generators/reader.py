def read_next(*args):
    for arg in args:
        yield ''.join(map(str, arg))


def read_next(*args):
    for collection in args:
        yield from collection


for item in read_next_2("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next_2("Need", (2, 3), ["words", "."]):
    print(i)
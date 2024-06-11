class ValueCannotBeNegative(Exception):
    """Raised when the user gives a negative number"""


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative

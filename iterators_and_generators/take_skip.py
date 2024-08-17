class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.count:
            num = self.current_index * self.step
            self.current_index += 1
            return num
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

# import unittest
#
# class TakeSkipTests(unittest.TestCase):
#     def test_zero(self):
#         numbers = take_skip(2, 6)
#         res = []
#         for number in numbers:
#             res.append(number)
#         self.assertEqual(res, [0, 2, 4, 6, 8, 10])
#
# if __name__ == '__main__':
#     unittest.main()
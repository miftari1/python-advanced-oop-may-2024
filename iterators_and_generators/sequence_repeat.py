class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            current_idx = self.current_index
            self.current_index += 1
            self.number -= 1
            try:
                return self.sequence[current_idx]
            except IndexError:
                self.current_index = 1
                return self.sequence[0]

        raise StopIteration


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
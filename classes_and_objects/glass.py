class Glass:
    # Class variable
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        # Fills the glass with the given quantity if there is enough space available
        new_content = self.content + ml

        if new_content <= Glass.capacity:
            self.content = new_content
            return f'Glass filled with {ml} ml'

        return f'Cannot add {ml} ml'

    def empty(self):
        # Empties the glass
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        # Returns an information about the available space in the glass
        space_left = Glass.capacity - self.content
        return f'{space_left} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
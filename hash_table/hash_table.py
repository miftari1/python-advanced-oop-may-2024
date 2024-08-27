class HashTable:
    def __init__(self, capacity: int = 4):

        self._capacity = capacity
        self._array = [None] * self._capacity
        self._num_items = 0
        self._max_load = 0.5

    def _find(self, key):
        # Returns an integer index to a cell with the key being sought
        idx_to_search = self.hash(key)

        # Iterates through every cell's index which the quadratic probe generator yields
        for i in self._quadratic_probe(idx_to_search, self._capacity):
            if self._array[i] is None or (self._array[i] is not None and self._array[i][0] == key):
                return i

        return None

    def _get_current_load(self):
        return self._num_items / self._capacity

    @staticmethod
    def _quadratic_probe(start, size):
        for i in range(size):
            yield (start + i ** 2) % size

    @staticmethod
    def is_prime(size):
        for i in range(2, size//2 + 1):
            if size % i == 0:
                return False
        return True

    def _grow_table(self):
        old_table = self._array

        self._capacity = len(old_table) * 2 + 1
        while not self.is_prime(self._capacity):
            self._capacity += 2

        self._array = [None] * self._capacity
        self._num_items = 0

        for i in range(len(old_table)):
            if old_table[i] is not None:
                self.add(*old_table[i])

    def hash(self, key: str):
        return hash(key) % self._capacity

    def add(self, key: str, value: any):
        index_to_add = self._find(key)

        if self._array[index_to_add] is None:
            self._array[index_to_add] = (key, value)
            self._num_items += 1

            if self._get_current_load() >= self._max_load:
                self._grow_table()

        if self._array[index_to_add] and self._array[index_to_add][0] == key:
            self._array[index_to_add] = (key, value)

    def get(self, key: str):
        index_to_get = self._find(key)

        if index_to_get is not None:
            return self._array[index_to_get][1]

        return 'Could not find item'

    def delete(self, key):
        idx_to_delete = self._find(key)

        if idx_to_delete is None or self._array[idx_to_delete] is None or self._array[idx_to_delete][0] != key:
            return 'Could not find item to delete'

        self._array[idx_to_delete] = None
        self._num_items -= 1

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __len__(self):
        return self._num_items

    def __repr__(self):
        return ', '.join([f'{el[0]}: {el[1]}' for el in self._array if el is not None])


table = HashTable()
table["name"] = "Peter"
table["age"] = 25
table['sex'] = 'Male'
print(table)
print(table.get("name"))
print(table["age"])
print(table.get('sex'))
table['position'] = 'engineer'
print(table['position'])
table['Date of birth'] = '22.11.1999'
print(table.get('Date of birth'))
table['courses'] = 'Python'
print(table.get('courses'))
table['pets'] = 'dog'
print(table.get('pets'))
table['pets'] = 'cat'
print(table.get('pets'))
table['sports'] = 'football'
table['sports'] = 'baseball'
table.delete('sports')
print(table)
print(len(table))

class PhotoAlbum:
    import math

    PAGE_CAPACITY = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = cls.math.ceil(photos_count / cls.PAGE_CAPACITY)
        return cls(pages)

    def add_photo(self, label: str):
        """Adds the photo in the first possible page and slot"""
        for page_index in range(len(self.photos)):
            if len(self.photos[page_index]) < 4:
                self.photos[page_index].append(label)

                page_num = page_index + 1
                slot_number = self.photos[page_index].index(label) + 1

                return f"{label} photo added successfully on page {page_num} slot {slot_number}"

        # If there are no free slots left
        return "No more free slots"

    def display(self):
        result = []
        if self.photos:
            for page in self.photos:
                result.append('-' * 11)
                result.append(' '.join(['[]' for _ in range(len(page))]))
            result.append('-' * 11)

        return '\n'.join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())



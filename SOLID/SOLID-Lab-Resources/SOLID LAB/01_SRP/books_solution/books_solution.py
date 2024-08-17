class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class BookLocation:
    def __init__(self, location):
        self.location = location

    def find_book(self):
        return self.location
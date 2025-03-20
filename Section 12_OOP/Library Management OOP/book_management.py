class Admin:
    def __init__(self, name):
        self.books_collection = {}

    def add_book(self, title, author, genre, ISBN: str, copies: int):
        self.books_collection[ISBN] = {
            "isbn": ISBN,
            "title": title,
            "author": author,
            "genre": genre,
            "copies": copies,
        }

    def update_book(self, update_list, isbn):
        for criteria, value in update_list.items():
            self.books_collection[isbn].update({criteria: value})

    def delete_book(self, isbn):
        self.books_collection.pop(isbn)

    def search_book(self, search_item):
        pos = None
        for key1, book_info in self.books_collection.items():
            for key2, value in book_info.items():
                if value == search_item:
                    pos = key1
                    break
            if pos:
                break
        print("The details of the book is {}".format(self.books_collection[pos]))

    def book_storage(self):
        for key, book_info in self.books_collection.items():
            print("{} {}".format(key, book_info))

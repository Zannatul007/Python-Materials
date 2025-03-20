class Admin:
    def __init__(self, name):
        self.books_collection = {}

    def add_book(self, title, author, genre, ISBN, copies: int):
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

    def search_book(self, search_criteria):
        for key,book_info in self.books_collection.items():
            if(book_info[])

    def book_storage(self):
        for key, book_info in self.books_collection.items():
            print("{} {}".format(key, book_info))

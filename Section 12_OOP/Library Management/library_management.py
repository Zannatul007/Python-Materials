class Book:

    def __init__(self, isbn, title, author, genre, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return " ISBN {}\n Title {}\n Author {}\n Genre {}\n Copies {}\n".format(
            self.isbn, self.title, self.author, self.genre, self.copies
        )


class User:
    def __init__(self, m_id, m_name, m_email, m_role="Member"):
        self.m_id = m_id
        self.m_name = m_name
        self.m_email = m_email
        self.m_role = m_role
        self.borrowed_books = {}

    def borrow_book(self, book: Book):
        self.borrowed_books[book.isbn] = book
    def return_book(self,book:Book):
        if book.isbn in self.borrowed_books:
            
            

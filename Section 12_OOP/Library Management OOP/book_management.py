class Admin:
    def __init__(self, name):
        self.books_collection = {}
        self.member_collection = {}

    ## Member Management by Admin
    def add_member(self, m_name, m_contact, m_id, member=None):
        self.member_collection[m_id] = {
            "m_id": m_id,
            "m_name": m_name,
            "m_contact": m_contact,
        }

    def update_member(self, update_list, m_id):
        for criteria, value in update_list.items():
            self.member_collection[m_id].update({criteria: value})

    def delete_member(self, m_id):
        self.member_collection.pop(m_id)

    ##Book Management by Admin
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


class Member:
    def __init__(self, member_name, contact_info, membership_id):
        self.member_name = member_name
        self.contact_info = contact_info
        self.membership_id = membership_id

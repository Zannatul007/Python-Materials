import bcrypt


class User(object):
    def __init__(self):
        self.user_collection = {}

    def user_registration(self, uname: str, upassword: str, role: str):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(upassword, salt)
        self.user_collection[uname] = {
            "User Name": uname,
            "Password": hashed,
            "Role": role,
        }

    def user_login(self, uname: str, upassword: str):
        if uname in self.user_collection["User Name"]:
            password = bcrypt.hashpw(upassword, bcrypt.gensalt())
            if self.user_collection[uname]["Password"] == password:
                print("{} logged in successfully".format(self.uname))
            else:
                print("Incorrect Password")
        else:
            print("User not found !!!")


class Admin(User):
    def __init__(self, admin_name):
        self.admin_name = admin_name
        self.books_collection = {}
        self.member_collection = {}

    ## Member Management by Admin
    def add_member(self, m_name, m_contact, m_id, member=None):
        self.member_collection[m_id] = {
            "m_id": m_id,
            "m_name": m_name,
            "m_contact": m_contact,
        }
        if member is None:
            member = Member(m_name, m_contact, m_id)
        else:
            member = member
        return member

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
            "status": "Available",
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


class Member(User):
    def __init__(self, m_name, m_contact, m_id):
        self.m_name = m_name
        self.m_contact = m_contact
        self.m_id = m_id
        self.borrowed_books = {}

    def borrow_book(self, isbn, admin, borrow_date, due_date):
        if (admin.books_collection[isbn]["copies"] > 0) and (
            isbn in admin.books_collection
        ):
            admin.books_collection[isbn]["copies"] -= 1
            self.borrowed_books[self.m_id] = {
                "isbn": isbn,
                "borrow_date": borrow_date,
                "due_date": due_date,
            }

        else:
            print("This book is unavailable")

    def return_book(self, isbn, admin):
        if isbn in self.borrowed_books[self.m_id]:
            del self.borrowed_books[self.m_id]["isbn"]
            admin.books_collection[isbn]["copies"] += 1
        else:
            print("This book has not borrowed")

class Admin:
    def __init__(self, name):
        self.name = name
        self.books_collection = {}
        self.member_collection = {}

    # Member Management By Admin
    def add_member(self, mname: str, mcontact: str, mid: str):
        self.member_collection[mid] = {
            "Member ID": mid,
            "Member Name": mname,
            "Member Contact": mcontact,
        }
        return Member(mname, mcontact, mid)

    def update_member(self, mid: str, update_list: dict):
        for criteria, value in update_list.items():
            self.member_collection[mid].update({criteria: value})

    def delete_member(self, mid: str):
        del self.member_collection[mid]

    # Book Management By Admin
    def add_book(self, title: str, author: str, genre: str, ISBN: str, copies: int):
        self.books_collection[ISBN] = {
            "ISBN": ISBN,
            "Book Title": title,
            "Book Author": author,
            "Genre": genre,
            "Copies": copies,
        }

    def update_book(self, ISBN: str, update_list: dict):
        for criteria, value in update_list.items():
            self.books_collection[ISBN].update({criteria: value})

    def delete_book(self, ISBN: str):
        del self.books_collection[ISBN]

    def search_book(self, search_criteria):
        pos = None
        for isbn, book_info in self.books_collection.items():
            for key, value in book_info.items():
                if value == search_criteria:
                    pos = isbn
                    break
            break
        print("The details of the book is {}".format(self.books_collection[pos]))

    def book_storage(self):
        for key, book_info in self.books_collection.items():
            print("{} {}".format(key, book_info))


class Member:
    def __init__(self, mname: str, mcontact: str, mid: str):
        self.mname = mname
        self.mcontact = mcontact
        self.mid = mid
        self.borrowed_books = {}

    def borrow_books(self, isbn: str, admin: Admin, borrow_date: str, due_date: str):
        if (isbn in admin.books_collection) and (
            admin.books_collection[isbn]["Copies"] > 0
        ):

            admin.books_collection[isbn]["Copies"] -= 1
            print(admin.books_collection[isbn]["Copies"])
            self.borrowed_books[self.mid] = {
                "ISBN": isbn,
                "Borrowed Date": borrow_date,
                "Due Date": due_date,
            }
            print(
                "{} borrowed the book {}".format(
                    self.mname, admin.books_collection[isbn]["Book Title"]
                )
            )

        else:
            print("Sorry !!! This book is not available")
        # print("After borrowing")
        # admin.book_storage()

    def return_book(self, isbn: str, admin: Admin):
        if isbn in self.borrowed_books:
            del self.borrowed_books[isbn]
            admin.books_collection[isbn]["Copies"] += 1
            print(
                "{} Returned the book {}".format(
                    self.mname, admin.books_collection[isbn]["Book Title"]
                )
            )
        else:
            print("Book is not borrowed")
        # print("After Returning")
        # admin.book_storage()

import json

# book_id = 0
# books_collection = {}

try:
    with open(
        "D:\Python Materials\library_management\library_data.json",
        "r",
        encoding="utf-8",
    ) as read_file:
        books_collection = json.load(read_file)
        book_id = len(books_collection)
except json.JSONDecodeError:
    books_collection = {}
    book_id = 0


def add_book(title: str, author: str):
    global book_id
    book_id += 1
    books_collection[book_id] = {
        "title": title,
        "author": author,
        "status": "Available",
    }


def check_out(id1: int, b_name: str, d_date: str):
    if id1 in books_collection:
        if books_collection[id1]["status"] == "Available":
            books_collection[id1]["status"] = "Checked out"
            books_collection[id1]["b_name"] = b_name
            books_collection[id1]["d_date"] = d_date
            print("Book checked out successfully!")
        else:
            print(f"Book was checked out by {books_collection[id1]['b_name']} in past")
    else:
        print("Book doesn't exist")


def return_book(id1: int):
    if id1 in books_collection:
        if books_collection[id1]["status"] == "Checked out":
            books_collection[id1]["status"] = "Available"
            print("Book returned successfully")
        else:
            print("Book is not checked out")
    else:
        print("Book never exists in library")


def view_status():
    for id1, book_info in books_collection.items():
        if book_info["status"] == "Available":
            print(
                f"ID: {id1}, Title: {book_info['title']}, Author: {book_info['author']}, Status: {book_info['status']}"
            )
        else:
            print(
                f"ID: {id1}, Title: {book_info['title']}, Author: {book_info['author']}, Status: {book_info['status']} by {book_info['b_name']}"
            )


choice = ""
choice_list = [
    "Add Book",
    "Check Out Book",
    "Return Book",
    "View Library Status",
    "Exit",
]
for index, item in enumerate(choice_list):
    print(f"{index+1}:\t{item}")

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        add_book(title, author)
        print("Book added successfully!")

    elif choice == "2":
        b_id = int(input("Enter book ID to check out: "))
        b_name = input("Enter borrower's name: ")
        d_date = input("Enter due date (YYYY-MM-DD): ")
        check_out(b_id, b_name, d_date)

    elif choice == "3":
        b_id1 = int(input("Enter book ID to return: "))
        return_book(b_id1)

    elif choice == "4":
        view_status()

    elif choice == "5":
        break

with open("library_data.json", "w", encoding="utf-8") as json_file:
    json.dump(books_collection, json_file)

from library_management import *

input1 = input("Do you have any account?\n")

if input1.casefold() == "yes":
    username = input("Enter your name : ")
    password = input("Enter your password : ")
    user = User()
    User.user_login(username, password)
else:
    username = input("Enter your name : ")
    password = input("Enter your password : ")
    contact = input("Enter your contact info : ")
    role = input("Enter the role you want to do : ")
    role = role.casefold()
    user = User()
    user.user_registration(username, password, role, contact)
if user.user_collection[username]["Role"] == "admin":
    admin1 = Admin(username)
    print(admin1.name)
    admin1.add_book("OS", "Sabbir Ahmed", "CS", "CS101", 20)
    admin1.add_book("DS", "Zannatul Fardaush", "CS", "CS102", 20)
    admin1.add_book("OOP", "MUNNA Ahmed", "CS", "CS103", 20)
    admin1.book_storage()
    admin1.delete_book("CS101")
    admin1.book_storage()
    admin1.update_book("CS102", {"Genre": "SciFi"})
    admin1.book_storage()
    admin1.search_book("DS")


else:

    user1 = Member(username, password, contact)

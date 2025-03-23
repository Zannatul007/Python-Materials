from library_management import *

input1 = input("Do you have any account? Yes/No: ")
input1 = input1.casefold()

if input1 == "yes":
    print("Please login to your account")
    uname = input("Enter your name : ")
    upassword = input("Enter your password : ")
    user = User()
    user.user_login(uname, upassword)

elif input1 == "no":
    print("Please register a new account")
    uname = input("Enter your name : ")
    upassword = input("Enter your password : ")
    contact = input("Enter the contact info : ")
    role = input("Enter the role what you want to do : ")
    role = role.casefold()
    user = User()
    user.user_registration(uname, upassword, role, contact)

if user.user_collection[uname]["Role"] == "admin":
    admin = Admin(uname)
    choice_list = {
        1: "Add book",
        2: "Update book",
        3: "Delete book",
        4: "Search book",
        5: "Add member",
        6: "Update member info",
        7: "Delete Member",
        8: "Show the book list",
        9: "Show the member list",
        10: "Exit",
    }
    for k, v in choice_list.items():
        print("{}\t{}".format(k, v))

    while True:
        input3 = int(input("Enter your choice : \n"))
        if input3 == 1:
            bisbn = input("Enter Book ISBN : ")
            btitle = input("Enter Book Title : ")
            bgenre = input("Enter Book Genre : ")
            bauthor = input("Enter Book Author : ")
            bcopies = int(input("Enter the Number of Copies : "))
            admin.add_book(btitle, bauthor, bgenre, bisbn, bcopies)
        elif input3 == 2:
            bisbn = (input("Enter the ISBN of book which you want to update"))

        elif input3 == 3:
            bisbn = (input("Enter the ISBN of book which you want to delete"))
        
        elif input3 == 4:
            search_item = input("Enter the criteria you want to search")
        elif 


        elif input3 == 8:
            admin.book_storage()
        if input3 >= 10:
            break

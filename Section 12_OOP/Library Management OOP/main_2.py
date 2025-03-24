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
            bisbn = input("Enter the ISBN of the book you want to update: ")
            update_list = {}
            criterias = {"Book Title", "Book Author", "Genre", "Copies"}
            for i in criterias:
                update_criteria = input(
                    "Enter new field {} you want to change(or press enter to keep cuurrent one): ".format(
                        i
                    )
                )
                if update_criteria:
                    if update_criteria == "Copies":
                        update_list[i] = int(update_criteria)
                    else:
                        update_list[i] = update_criteria
                admin.update_book(bisbn, update_list)

        elif input3 == 3:
            bisbn = input("Enter the ISBN of the book you want to delete: ")
            admin.delete_book(bisbn)

        elif input3 == 4:
            search_item = input("Enter the criteria you want to search: ")
            admin.search_book(search_item)

        elif input3 == 5:
            mid = input("Enter member ID: ")
            mname = input("Enter member name: ")
            mcontact = input("Enter member contact info: ")
            admin.add_member(mname, mcontact, mid)

        elif input3 == 6:
            mid = input("Enter the Member ID of the book you want to update")
            update_list = {}
            criterias = ["User Name", "Password", "Contact", "Role"]
            for i in criterias:
                update_criteria = input(
                    "Enter new field {} you want to change (or press enter to keep the current one)".format(
                        i
                    )
                )
                if update_criteria:
                    update_list[i] = int(update_criteria)
                admin.update_member(mid, update_list)

        elif input3 == 7:
            mid = input("Enter the ID of the member you want to delete: ")
            admin.delete_member(mid)

        elif input3 == 8:
            admin.book_storage()

        elif input3 == 9:
            admin.member_list()

        elif input3 == 10:
            print("Exiting admin panel...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

elif user.user_collection[uname]["Role"] == "member":
    choice_list = {
        1: "Borrow book",
        2: "Return book",
    }
    for k, v in choice_list.items():
        print("{}\t{}".format(k, v))

    while True:
        input3 = int(input("Enter your choice : \n"))

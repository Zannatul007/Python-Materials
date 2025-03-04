available_parts = {
    "1":"Mouse",
    "2": "Keyboard",
    "3":"speaker",
    "4":"Cable",
    "5": "Modem",
    "6":"Gpu"
}

current_choice = ""
cart_list = []
while current_choice != "0":
    if current_choice in available_parts:
        print("Adding {}".format(available_parts[current_choice]))
        cart_list.append(available_parts[current_choice])

    else:
        for key,value in available_parts.items():
            print("{}:{}".format(key,available_parts[key]))
    current_choice = input(">")

print("New Cart List {}".format(cart_list))
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
        chosen_part = available_parts[current_choice]
        if chosen_part in cart_list:
            cart_list.remove(chosen_part)
        else:
            print("Adding {}".format(available_parts[current_choice]))
            cart_list.append(chosen_part)

    else:
        for key,value in available_parts.items():
            print("{}:{}".format(key,available_parts[key]))
        print ("0 for exit")
    current_choice = input(">")

print("New Cart List {}".format(cart_list))
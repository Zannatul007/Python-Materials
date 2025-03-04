available_parts = {
    "1":"Mouse",
    "2": "Keyboard",
    "3":"speaker",
    "4":"Cable",
    "5": "Modem",
    "6":"Gpu"
}

current_choice = None
computer_parts = {}
while(current_choice!='0'):
    current_choice = input(">")
    if(current_choice in available_parts):
        if(current_choice in computer_parts):
            print(f"Removing {available_parts[current_choice]}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {available_parts[current_choice]}")
            computer_parts[current_choice] = available_parts[current_choice]
    else:
        for key,value in available_parts.items():
            print(f"{key}:{value} ")
        print("0: Exit")
        
print(computer_parts)
available_parts = ["disk","mouse","speaker","headphone","cables"]
valid_choices = []
new_parts =[]
choice = '-1'
for i in range(len(available_parts)):
    valid_choices.append(str(i+1))
print(valid_choices)
while (choice != '0'): 
    if(choice in valid_choices):
        print("Adding choice {}".format(choice))
        index = int(choice)-1
        print(index)
        new_parts.append(available_parts[index])
    else:
        print("Please select items from this list ")
        for number,part in enumerate(available_parts):
            print("{}:{}".format(number+1,part))



    choice = input()

print(new_parts)
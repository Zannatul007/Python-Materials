input_numbers = input("Please enter three numbers, separated by commas:")
splitted_number_list = input_numbers.split(',')
int_number_list = []
for i in splitted_number_list:
    int_number_list.append(int(i))
a = int_number_list[0]
b = int_number_list[1]
c = int_number_list[2]

print(a+b-c)

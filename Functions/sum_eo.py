def sum_eo(t,n):
    integer_list = []
    sum_e = 0
    sum_o= 0
    print("Please make a list of numbers \n")
    for i in range(0,n):
        input_int = int(input())
        integer_list.append(input_int)
    for j in integer_list:
        if(j%2==0):
            sum_e+=j
        else:
            sum_o+=j
    if(t == 'e'):
        return sum_e
    elif(t=='o'):
        return sum_o
    else:
        return -1
    

user_input_sum = sum_eo('o',6)
print(user_input_sum)

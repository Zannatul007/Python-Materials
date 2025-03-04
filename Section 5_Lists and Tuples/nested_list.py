even = [2,4,6,8,10]
odd = [1,3,5,7,9]

new_list = even+odd
print(new_list)
new_list.sort()
print(new_list)


new_list_2 = [even,odd]
print(new_list_2)
print("---"*20)
for i in new_list_2:
    print(i)
print("+"*90)
for i in new_list_2:
    print(i)
    for j in i:
        print(j)
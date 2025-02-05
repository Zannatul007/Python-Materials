list1 = ["milk","pasta","eggs","spam","bread"]

list2 = list1
print(list2)

print(id(list1))
print(id(list2))


list1+=['cookie']
print(list1)

a = b = c = d = e = list1
print(a)

list1.append('bun')
print(b)


print("id_list1{},id_list2{},id_a{},id_b{}".format(id(list1),id(list2),id(a),id(b)))
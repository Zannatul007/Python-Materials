inp1 = int(input())
list_1 = []

for i in range(0,inp1):
    inp2 = int(input())
    list_1.insert(i,inp2)
tuple_1 = tuple(list_1)
print(hash(tuple_1))
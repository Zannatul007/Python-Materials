#set creation

# set1 = {*""}
# print(type(set1))
# set2 = {'{}'}
# print(type(set2))
# set3 = set()
# print(type(set3))
# unknown = {}
# print(type(unknown))

#Adding items to set
data ={"a","b","c"}
print(len(data))

# while len(data)<=6:
#     inp1 = int(input("Add next value to the set :"))
#     data.add(inp1)
# print(data)

#modifying set

farm = {"cow","cat","goat","dumba","cow","dumba"}
print(farm)
print(sorted(farm))

#preserve the original order of set we can use dict.fromkeys-> from keys also maintain the order of keys how it inserted
preserved_position = list(dict.fromkeys(farm))
print(preserved_position)
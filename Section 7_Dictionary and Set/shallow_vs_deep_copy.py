import copy 
dict1 = {
    'model':"bmw",
    "color":["blue","green","silver"],
    "year":2020
}

# dict2_shallow = dict1.copy()
# dict1['color'].append("black")
# print(dict2_shallow)
# print(dict1)

# dict2_direct_copy = dict1
# print("--"*20)
# dict1['color'].append("pink")
# print(dict2_direct_copy)
# print(dict1)

dict2_deep_copy = copy.deepcopy(dict1)
dict1["color"].append("white")
print(dict1)
print("--"*100)
print(dict2_deep_copy)


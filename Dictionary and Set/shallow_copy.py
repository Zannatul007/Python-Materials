dessert_list = ['payesh','chomchom','pudding']
main_list = ['beef','chicken','vegetables']
side_list = ["bhorta","daal","salad"]

food_dict = {
    "dessert":dessert_list,
    "main" : main_list,
    "side" :side_list,
}

#performing shallow copy
new_dict = food_dict.copy()

new_dict['dessert'].append("golap jamun")
# dessert_list.append("patishapta")

food_dict['dessert'].append("foody golab jamun")

# print(new_dict)
# print(food_dict)


dict1 = {'a': 10, 'b': 'hello'}
dict2 = dict1.copy()  # Shallow copy

dict2['a'] = 20  # Changing copied dictionary

print(dict1)  # {'a': 10, 'b': 'hello'}
print(dict2)  # {'a': 20, 'b': 'hello'}

#performing deep copy
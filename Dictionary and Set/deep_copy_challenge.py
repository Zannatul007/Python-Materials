import copy
def my_deepcopy(d: dict)-> dict:
    new_dict = {}
    for key,value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict

original ={
    "Zannatul":["SWE",["PYTHON","C++"],"Bangladesh"],
    "Meem":["SWE",["React","CSS","C++"],"Bangladesh"],
}

copy2 = copy.deepcopy(original)
copy1 = my_deepcopy(original)
copy1["Zannatul"][1].append("Java")

# print(copy1)
# print(copy2)
# print(original)


print("__"*50)

copy_test_1 = my_deepcopy(original)
print(copy_test_1)
original['Zannatul'][1] = ['10']
print(original)
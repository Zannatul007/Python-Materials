recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}


for recipe,ingredients in recipes_tuple.items():
    print("The ingredients of `{}` are".format(recipe))
    for ingredient,quantity in ingredients:
        print(ingredient,quantity,sep=", ")

for r,i in recipes_dict.items():
    print("The ingredients of `{}` are".format(r))
    for i,q in i.items():
        print(i,q,sep=", ")

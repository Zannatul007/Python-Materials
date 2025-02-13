from contents import recipes, pantry
selected_meal = {}
choice = " "
for index,key in enumerate(recipes):
    selected_meal[str(index+1)] = key

while True:
    print("Please Select Your Recipe")
    print("----"*10)
    choice = input(":")
    if choice == "0":
        break
    elif choice in selected_meal:
        recipe_name = selected_meal[choice]
        print(f"You have chosen {recipe_name}")
        ingredients = recipes[recipe_name]
        print(f"The ingredients list is {ingredients}")
        for food_item,required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item,"0")
            if  required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK ")
            else:
                print(f"Ingredient `{food_item}` {required_quantity-quantity_in_pantry} is needed")


    for key,values in selected_meal.items():
        print("{}:{}".format(key,values))


print(recipes)
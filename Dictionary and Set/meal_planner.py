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
        for food_item in ingredients:
            if food_item in pantry:
                print(f"\t{food_item} OK : Quantity {pantry[food_item]} ")
            else:
                print(f"Ingredient {food_item} is missing1")


    for key,values in selected_meal.items():
        print("{}:{}".format(key,values))


print(recipes)
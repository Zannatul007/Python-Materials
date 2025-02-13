from contents import recipes,pantry


choice = "-"
selected_meal = {}
shopping_list = {}
while choice!="0":
    choice = input(":")
    for index,key in enumerate(recipes):
        selected_meal[str(index+1)] = key
    
    if choice in selected_meal:
        recipe_name = selected_meal[choice]
        print("You have selected `{}`".format(recipe_name))
        ingredients = recipes[recipe_name]
        for food_item,required_quantity in ingredients.items():
            available_quantity = pantry.get(food_item,0)
            if (required_quantity<=available_quantity):
                print("`{}` is available for recipe".format(food_item))
            else:
                quantity_needed = required_quantity-available_quantity
                print("`{}` is not enough : Need {} units".format(food_item,quantity_needed))
                shopping_list[food_item] = shopping_list.get(food_item,0)+quantity_needed 

        
for item,quantity in shopping_list.items():
    print(f"`{item}`: `{quantity}`")
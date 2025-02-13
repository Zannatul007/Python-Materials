from contents import recipes,pantry


choice = "-"
selected_meal = {}
shopping_list = {}
while choice!="0":
    
    for index,key in enumerate(recipes):
        selected_meal[str(index+1)] = key
    print("----"*20)
    for index,value in selected_meal.items():
         print(f"{index} : {value}")
    choice = input(":")
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
                #.get --> if the key is not exist in the dict then it doesn't create another key it just giving the default value
                #shopping_list[food_item] = shopping_list.get(food_item,0)+quantity_needed 
                #.setdefault --> if there is no key present in the dictionary it by default create this key and assign the default value(here 0)
                shopping_list[food_item] = shopping_list.setdefault(food_item,0)+quantity_needed 
    


print("***Shopping List****")
        
for item,quantity in sorted(shopping_list.items()):
    print(f"`{item}`: `{quantity}`")
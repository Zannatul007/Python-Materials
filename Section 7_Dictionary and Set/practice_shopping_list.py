from contents import pantry,recipes

selected_recipe = {}
choice = ""
shopping_list = {}
for index,key in enumerate(recipes):
    selected_recipe[str(index+1)] = key
while choice !="0":
    
    for i in selected_recipe:
        print(f"{i}:{selected_recipe[i]}")
    if choice in selected_recipe:
        recipe_name = selected_recipe[choice]
        ingredients_list = recipes[recipe_name]
      
        for item,req_quantity in ingredients_list.items():
            available_quantity = pantry.get(item,0)
            if(req_quantity>=available_quantity):
                print(f"{item}:\t OK")
            else:
                print(f"{item}:\t Need {available_quantity-req_quantity}")
                shopping_list[item] = shopping_list.setdefault(item,0)+(available_quantity-req_quantity)

        
    for key,value in shopping_list.items():
        print(f"{key}:{value}")


    choice = input(">")


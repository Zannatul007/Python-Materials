# #clear() removes all the elements from the dictionary
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.clear()
# print(car)

# #copy() returns the copy of the dictionary 
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# carx = car.copy()
# print(carx)
# print("-"*80)
# y = car
# print(y)

# #fromkeys(keys,value)	Returns a dictionary with the specified keys and value
# #keys must be an iterable specifying 
# x = ['key1','key2','key3']
# y = 0

# z = dict.fromkeys(x,y)
# print(z)

# #get() Returns the value of the specified key
# print(carx.get("brand"))
# print(carx.get("price",15000))

# #items()Returns a list containing a tuple for each key value pair
# print(carx.items())


# #keys()	Returns a list containing the dictionary's keys
# print(carx.keys())
# x = carx.keys()
# carx["color"] = "Blue"
# print(x)

# #pop()
# popped=carx.pop("model","yuuck")
# print(popped)





##TIM BUCHALKA CODE 

d = {
    0:"Zero",
    1: "one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}
d2 ={
    6:"new six is here",
    0:"New Zero"
}
pantry = ["bread","chicken","spam"]

#update_values
print("1st Update \n")
d.update(enumerate(pantry))
print(d)
d.update(d2)
print("\n 2nd Update \n")
print(d)
print("\n 3rd update\n")
d[6] = "six"
print(d)


#items 
items_dict = d.items()
print(items_dict)
#values
value = list(d.values())
#key values
key = list(d.keys())

if "four" in value:
    index = value.index("four")
    print(index)
    key = key[index]
    
    print(f"{d[key]} is found with {key}")
print(value)



#changed keys values 
keys = dict.fromkeys(pantry,0)
print(keys)
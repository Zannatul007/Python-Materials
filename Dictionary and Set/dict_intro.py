vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

#access by indexing(using key)
my_car = vehicles['fiesta']
print(my_car)

#access by get method
my_another_car = vehicles.get('jimny')
print(my_another_car)

#iterating over dictionaries

for key in vehicles:
    print("This car `{0}` has the key of `{1}`".format(vehicles[key],key))


#adding items 
vehicles['bmw'] ="cvc :/"
vehicles['honda'] = 'crv 2025'

#delete items from dictionary
#using del 
del vehicles['dream']

#using pop 
popped_bmw = vehicles.pop('bmw',"Not present Now")
print(popped_bmw)
popped_bmw_again = vehicles.pop('bmw',"Not present Now")
print(popped_bmw_again)
#another way to iterate dictionaries
for key,value in vehicles.items():
    print("Key {} : Vehicle {}".format(key,value))



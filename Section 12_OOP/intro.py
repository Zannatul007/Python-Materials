class Kettle(object):
    def __init__(self,make,price):
        self.make = make 
        self.price = price 
        self.on = False
    def switch_on(self):
        self.on = True
        

kenwood = Kettle('Kenwood',100)
print(kenwood.price)
print(kenwood.make)

kenwood.price = 200
print(kenwood.price)

hamilton = Kettle('Hamilton',200)
print("{0.make} = {0.price}\t{1.make} = {1.price}".format(kenwood,hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print('--'*90)

Kettle.switch_on(kenwood)
print(kenwood.on)

#kenwood.power = 1.5 creates a new attribute power only for the kenwood instance.
#n Python, you can dynamically add attributes to an instance of a class, even if they were not defined inside the __init__ method
kenwood.power = 1.5
print(kenwood.power)

print(hamilton.power)#give error . Because power attribute is only built for 'kenwood' instance

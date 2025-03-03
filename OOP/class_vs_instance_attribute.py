#attributes define the properties of objects.
# They can be classified into class attributes and instance attributes based on how they are stored and accessed.

""" Class Attributes
Defined inside the class but outside any method.
Shared by all instances of the class.
Changing a class attribute affects all instances (unless overridden in an instance).
 """

class Kettle(object):
    power_source = "electricity"
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False
        
    def switch_on(self):
        self.on = True

kenwood = Kettle('Kenwood',14.99)
hamilton = Kettle('Hamilton',15)

print(kenwood.power_source)
print(hamilton.power_source)

Kettle.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

"""Instance Attributes
Defined inside the __init__ method using self.
Unique to each instance.
Modifying an instance attribute only affects that specific instance."""

# Modifying an instance attribute
kenwood.price = 150
print(kenwood.price)  # Output: 150 (only changed for kenwood)
print(hamilton.price)  # Output: 15 (remains unchanged)

""" What Happens If an Instance Modifies a Class Attribute?
If an instance modifies a class attribute, it creates a new instance attribute with the same name,
 rather than modifying the original class attribute."""

kenwood.power_source = "Solar" # Creates a new instance attribute
print(kenwood.power_source)
print(hamilton.power_source)

"""🚀 When to Use Which?
Use class attributes when a property should be shared by all instances (e.g., power_source).
Use instance attributes when a property should be unique to each instance (e.g., price and make)."""

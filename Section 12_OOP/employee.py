class Employee:
    # Class attribute (shared by all instances)
    raise_amount = 1.05  
    no_of_employees = 0  # Tracks total number of employees created

    def __init__(self, fname, lname, pay):
        """
        Constructor method (__init__) that initializes the employee instance.
        """
        self.fname = fname  # Instance attribute for first name
        self.lname = lname  # Instance attribute for last name
        self.pay = pay  # Instance attribute for salary
        self.mail = fname + '.' + lname + '@' + 'gmail.com'  # Email generated using first & last name

        Employee.no_of_employees += 1  # Increments the class attribute (shared counter)

    def fullname(self):
        """
        Returns the full name of the employee.
        """
        return self.fname + ' ' + self.lname

    def amount_raise(self):
        """
        Returns the increased salary after applying the raise.
        Using Employee.raise_amount (class attribute).
        """
        return int(self.pay*self.raise_amount)# Using instance attribute, not class attribute
        # return int(self.pay * Employee.raise_amount)  # Using class attribute, not instance attribute


# Creating first Employee instance
emp1 = Employee('Zannatul', 'Fardaush', 100)

# Printing raised salary using class attribute
print(emp1.amount_raise())  # Output: 105 (100 * 1.05)

# Printing raise_amount accessed from instance (inherits from class)
print(emp1.raise_amount)  # Output: 1.05

# Printing full name
print(emp1.fullname())  # Output: Zannatul Fardaush

# Printing instance attributes (stored in __dict__)
print(emp1.__dict__)  # Shows only instance attributes, NOT class attributes

# Creating an instance-level attribute (shadowing class attribute)
emp1.raise_amount = 1.04  # This does NOT modify class attribute, but adds a new instance attribute

# Now, emp1 has its own raise_amount attribute
print(emp1.raise_amount)  # Output: 1.04

# This still uses the class attribute because the method refers to Employee.raise_amount
print(emp1.amount_raise())  # Output: 105 (not affected by emp1.raise_amount)

# Printing instance dictionary again, now it contains `raise_amount`
print(emp1.__dict__)  # Shows `raise_amount: 1.04` added at instance level

# Printing class dictionary (does not include instance-specific attributes)
print(Employee.__dict__)  # Contains class attributes like `raise_amount` and `no_of_employees`


# Creating second Employee instance
emp2 = Employee("Saima", "Murtuza", 200)

# Printing full name
print(emp2.fullname())  # Output: Saima Murtuza

# emp2 does NOT have a `raise_amount` attribute, so it inherits from class
print(emp2.raise_amount)  # Output: 1.05 (from class attribute)

# Printing emp2's instance dictionary (will NOT contain raise_amount because it wasn’t modified)
print(emp2.__dict__)  # Only contains `fname`, `lname`, `pay`, and `mail`

# Calculating raise for emp2 (still using Employee.raise_amount = 1.05)
print(emp2.amount_raise())  # Output: 210 (200 * 1.05)


# Printing total number of employees (class attribute)
print(Employee.no_of_employees)  # Output: 2 (emp1 and emp2 created)

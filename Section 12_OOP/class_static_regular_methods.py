import datetime
class Employee:
    raise_amount = 1.05
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+'.'+lname+'@gmail.com'
        self.fullname = fname+' '+lname

    def fullname(self):
        return self.fname+' '+self.lname
    def amount_raised(self):
        return (float(self.pay*self.raise_amount))
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

emp1 = Employee('Zannatul','Fardaush',2000)
emp2 = Employee('Zannatul','Fardaush Tripty',2000)
print(emp1.fullname)
print(emp1.email)
print(emp1.amount_raised())


Employee.raise_amount = 1.05
emp1.raise_amount = 1.04

print(emp1.raise_amount)
print(emp2.raise_amount)


Employee.set_raise_amount(1.08)
print(Employee.raise_amount)
print(emp1.raise_amount)#not changed 1.04
print(emp2.raise_amount)


employee_string = "Zannatul-Fardaush Zane-2000"
emp3 = Employee.from_string(employee_string)
# print(data)
# emp3 = Employee(data[0],data[1],data[2])
# print(emp3.fname)
# print(emp3.fullname)
print(emp3.fullname)


my_date = datetime.date(2016, 7,10)
print(Employee.is_workday(my_date))
        
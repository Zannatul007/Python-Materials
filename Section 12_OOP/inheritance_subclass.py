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
#     """Static Methods (@staticmethod)
# Do not depend on the class or instance.
# Work like regular functions inside a class.
# """
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
class Developer(Employee):
    raise_amount = 1.07
    def __init__(self, fname, lname, pay,programming_lang):
        super().__init__(fname, lname, pay)
        # Employee.__init__(self,fname,lname,pay)
        self.programming_lang = programming_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees = None):
        super().__init__(fname, lname, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees
    def supervised_add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def supervised_remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname)




dev1 = Developer('Zannatul','Fardaush',900,"Python")
dev2 = Developer('Zannatul','Fardaush Tripty',900,"Python+(C++)")
dev3 = Developer('Munna','Bhai',1000,"Python")
dev4 = Developer('Biplob','Bhai',1000,"Python")
print(dev1.fullname+'\n'+dev1.email+'\n'+dev1.programming_lang)
print(Employee.raise_amount)
print(dev1.raise_amount)


manager_1 = Manager('Sabbir','Ahmed',2700,[dev1])
manager_1.supervised_add_emp(dev2)
manager_1.supervised_add_emp(dev3)
manager_1.supervised_add_emp(dev4)
manager_1.print_emp()


print(isinstance(manager_1,Manager))
print(issubclass(Manager,Employee))
class Employee:
    raise_amt = 1.04
    num_of_employees = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@gmail.com"
        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def amount_raised(self):
        return float(self.pay) * self.raise_amt

    @classmethod
    def from_str(cls, emp_str):
        f, l, p = emp_str.split("-")
        return cls(f, l, p)

    @classmethod
    def change_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def address(adress):
        return adress


class Developer(Employee):
    def __init__(self, fname, lname, pay, programming_lang):
        super().__init__(fname, lname, pay)
        self.programming_lang = programming_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []

    def supervised_add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def supervised_remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_devs(self):
        for emp in self.employees:
            print(
                "Name of the Employee is {} under {} supervison".format(
                    emp.fullname(), self.fullname()
                )
            )


emp1 = Employee("Zannatul", "Tripty", "10000")
print(emp1.fullname())
print(emp1.email)
print(f"Basic {emp1.pay}")
print(f"Incremented by 4% {emp1.amount_raised()}")
Employee.change_raise_amt(1.05)
print(f"Incremented by 5% {emp1.amount_raised()}")
print(emp1.address("772/AVAENU6/DOHS"))

emp2_str = "Nushrat-Jahan-20000"
emp2 = Employee.from_str(emp2_str)
print(emp2.fullname())


print("-" * 80)
dev1 = Developer("Munna", "Hossen", 25000, "Python")
print(dev1.programming_lang)
print(dev1.pay, dev1.amount_raised(), dev1.email, dev1.fullname())


dev1 = Developer("Munna", "Hossen", 25000, "Python")
dev2 = Developer("Biplob", "Hossen", 30000, "Java")
dev3 = Developer("Zannatul", "Fardaush", 28000, "C++")
manager1 = Manager("Sabbir", "Ahmed", 100000)

manager1.supervised_add_emp(dev1)
manager1.supervised_add_emp(dev2)
manager1.supervised_add_emp(dev3)
manager1.show_devs()

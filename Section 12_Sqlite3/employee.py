class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp1 = Employee("Zannatul", "Fardaush", 10000)
emp2 = Employee("Zerin", "Shaima", 50000)

# print(emp1.email(), emp1.fullname())
# print(emp2.email(), emp2.fullname())

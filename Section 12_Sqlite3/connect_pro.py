import sqlite3
from employee import Employee

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE employee (id INT PRIMARY KEY,first TEXT,last TEXT,pay INT)")


class Employee:
    def __init__(self, e_id, first, last, pay):
        self.id = e_id
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    def fullname(self):
        return "{} {}".format(self.first, self.last)


class Admin:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        self.employees[emp.id] = emp

        with conn:
            c.execute(
                "INSERT INTO employee (id,first,last,pay) VALUES (:id,:first,:last,:pay)",
                {"id": emp.id, "first": emp.first, "last": emp.last, "pay": emp.pay},
            )

    def show_employees(self):
        with conn:
            c.execute("SELECT * FROM employee")
        return c.fetchall()

    def update_employee(self, emp, pay):
        with conn:
            c.execute(
                "UPDATE employee SET pay=:pay WHERE id = :id",
                {"pay": pay, "id": emp.id},
            )

    def delete_employee(self, emp):
        with conn:
            c.execute("DELETE FROM employee WHERE id = :id", {"id": emp.id})


emp1 = Employee("E101", "Zannatul", "Fardaush", 10000)
emp2 = Employee("E102", "Zerin", "Shaima", 50000)
admin1 = Admin()
admin1.add_employee(emp1)
admin1.add_employee(emp2)
print(admin1.show_employees())
print("AFTER UPDATE")
admin1.update_employee(emp1, 20000)
print(admin1.show_employees())
print("AFTER DELETE")
admin1.delete_employee(emp2)
print(admin1.show_employees())

import sqlite3
from employee import Employee

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE employee(first text,last text,pay int)")

emp1 = Employee("Zannatul", "Fardaush", 10000)
emp2 = Employee("Zerin", "Shaima", 50000)

# c.execute(
#     "INSERT INTO employee (first,last,pay) VALUES (:first,:last,:pay)",
#     {"first": emp1.first, "last": emp1.last, "pay": emp1.pay},
# )

# DB API METHOD
# c.execute(
#     "INSERT INTO employee (first,last,pay) VALUES (?,?,?)",
#     (emp1.first, emp1.last, emp1.pay),
# )
# More suitable method (placeholder)
c.executemany(
    "INSERT INTO employee (first,last,pay) VALUES (:first,:last,:pay)",
    [
        {"first": emp1.first, "last": emp1.last, "pay": emp1.pay},
        {"first": emp2.first, "last": emp2.last, "pay": emp2.pay},
    ],
)
conn.commit()

c.execute("SELECT * FROM employee WHERE last=:last", {"last": "Fardaush"})
# c.execute("SELECT * FROM employee")
print(c.fetchall())

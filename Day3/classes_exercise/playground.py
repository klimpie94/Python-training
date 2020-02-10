import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first=None, last=None, pay=None):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@linkit.nl"

        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, num=1.11):
        cls.raise_amount = num

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __add__(self, other):
        return self.pay + other.pay

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} {}".format(self.fullname, self.email)

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# print(help(Developer))


# day = datetime.datetime.now()
# print(Developer.is_workday(day))

    
# print(Employee.num_of_emps)
emp1 = Developer("Test", "User", 50000, "python")
emp2 = Developer("Dana", "Arsovska", 70000, "scala")

print(repr(emp2))
print(str(emp2))
print(emp2.fullname)
# print(emp1 + emp2)
# print(Employee.num_of_emps)

# print(emp2.pay)
# Employee.set_raise_amount(1.10)
# emp2.apply_raise()
# print(emp2.pay)

# print(emp2.raise_amount)

# print(emp2.fullname())

# print(emp1.email)
# print(emp2.first)
# print(emp2.pay)
# print(emp2.email)

# emp_3_str = "Alexia-Wu-15000"
# emp_4_str = "Will-Smith-50000"
# emp_5_str = "Adam-Jones-35000"

# emp3 = Employee.from_string(emp_3_str)

# print(emp3.fullname())

# first, last, pay = emp_3_str.split("-")

# emp_3 = Employee(first, last, pay)

# new comment
# print(emp_3.pay)
# print(emp_3.email)










# import datetime
# my_date = datetime.date(2020, 2, 10)

# print(Employee.is_workday(my_date))



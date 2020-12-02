class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@yahoo.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
emp1 = Employee("Shahzaib", "rind", 230)
emp2 = Employee("Miraj", "rind", 2302)

import datetime
my_date = datetime.date(2020, 7, 26)
print(Employee.is_workday(my_date))

emp_str_1 = 'touqeer-siraj-43'
emp_str_2 = 'jabbar-rodanani-93'

new_emp1 = Employee.from_string(emp_str_1)
print(new_emp1.email)
print(new_emp1.pay)
Employee.set_raise_amount(1.06)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

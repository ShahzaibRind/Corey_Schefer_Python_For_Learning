class Employee:

    amount_raise = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@yahoo.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.amount_raise)

    # Dunder Methods

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Shahzaib", 'rind', 2500)
emp2 = Employee('Miraj', 'khan', 1500)

print("Salary of Both Employees is: ", emp1+emp2)
print(len(emp1))


# print(repr(emp1))
# print(str(emp1))
# # str(emp1)

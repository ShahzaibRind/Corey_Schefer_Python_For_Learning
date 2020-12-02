class Employee:
    no_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@Yahoo.com'
        self.pay = pay

        Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print('--->', emp.fullname())


emp1 = Developer("Shahzaib", "rind", 233, 'Python')
emp2 = Developer("Touqeer", "siraj", 232, 'Java')

mgr1 = Manager('Mirah', 'Khan', 90000, [emp1])

print(isinstance(mgr1, Developer))
print(issubclass(Developer, Employee))
# print(mgr1.email)
# mgr1.add_emp(emp2)
# mgr1.remove_emp(emp1)
# mgr1.print_emp()
# print('Emails is... ', emp1.email)
# print('Language is...', emp1.pro_lang)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# print(help(Developer))

class Employee:
    no_of_emp = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, sal, email):
        self.fname = fname
        self.lname = lname
        self.sal = sal
        self.email = fname + '.' + lname + '@gmail.com'

        Employee.no_of_emp += 1

    def Full_name(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.sal = int(self.sal * self.raise_amount)

emp1 = Employee("shahzaib", "rind", 2222, " ")
emp2 = Employee("Miraj", "Khan", 3333, " ")

print("Total Employees In Company: ", Employee.no_of_emp)
# emp1.raise_amount = 1.05
#
# print(emp1.__dict__)
# print(emp2.raise_amount)
# print(emp1.raise_amount)
# # print(emp1.Full_name())
# print(emp1.email)
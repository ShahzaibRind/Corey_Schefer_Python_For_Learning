class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.first = None
        self.last = None


emp1 = Employee('Shahzaiab', 'rind')
emp1.fullname = 'Abdul Jabbar'

print('First name: ', emp1.first)
print('Full Name: ', emp1.fullname)
print('Email: ', emp1.email)


del emp1.fullname
class Employee:
    def __init__(self, name, address, salary):
        self.__salary = None
        self.name = name
        self.address = address
        self.salary = salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,other):
        if other>=1:
            self.__salary = other

    def __str__(self):
        return f'Class: Employee\n' \
            f'Name: {self.name}\n' \
            f'Address: {self.address}\n' \
            f'Salary: {self.salary}\n'

class Manager(Employee):
    def __init__(self, numOfUnderlings, name, address, salary):
        self.numOfUnderlings = numOfUnderlings
        super().__init__(name,address, salary)

    def __str__(self):
        return super().__str__() + f'Class: Manager, Number of underlings: {self.numOfUnderlings}'

guy = Manager(3,'Guy', 'Yavne', -20)
print(guy)
guy = Manager(3,'Guy', 'Yavne', 20)
print(guy)

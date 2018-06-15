#Abstract class
class EmpType(object):
    emp_type = 'General'
    def show_type(self):
        raise NotImplementedError('Subclass needs to implement this!')

# Base class
class Employee(object):
    name = '' # public variable
    _experience = 0 # protected variable
    __salary = 0 # private variable

    def __init__(self, name, experience, salary):
        self.name, self._experience, self.__salary = name, experience, salary

    def show_details(self):
        print('Employee name: ' + self.name +
              ', Experience: ' + str(self._experience) +
              ', Salary: ' + str(self.__salary))


# Derived class
class Developer(Employee, EmpType):
    def __init__(self, name, experience, salary):
        return super().__init__(name, experience, salary)

    def show_type(self):
        self.emp_type = 'Developer'
        print('Employee is ' + self.emp_type)


# Derived class
class QA(Employee, EmpType):
    def __init__(self, name, experience, salary):
        return super().__init__(name, experience, salary)

    def show_type(self):
        self.emp_type = 'QA'
        print('Employee is ' + self.emp_type)

try:
    #Base class object
    em = Employee('Rahim', 9, 180000)
    em.show_details()

    #Derive class objects
    emps = [Developer('Karim', 8, 240000), QA('Alom', 7, 220000)]

    for emp in emps:
        emp.show_details()
        emp.show_type()

    #print(qa.name, qa._experience) #public and protected can access

except Exception as e:
    print(e)

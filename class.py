class Employee():
    def __init__(self,first,last): #self takes the form of the instance that invokes the init method .In our case when emp1 is created self takes the form of emp1 and as is the case for emp2
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@companyname'

    def fullname(self):   #arguementany method within a class automatically takes its instance as first 
        return ('{} {}').format(self.first , self.last)

emp1 = Employee('alanakr','parajuli')

emp2 = Employee('raknala','ilujarap')

print(emp1.first)
print(emp2.first)
print(emp1.fullname())
#print(Employee.fullname(emp1)) #if class name is used to call the method within it , its instance should be passed as a argument
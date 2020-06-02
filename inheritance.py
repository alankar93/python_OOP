class Employee: #parent class
    def __init__(self,first,last,salary):
        self.first=first
        self.last = last
        self.salary=salary

    def fullName(self):
        return '{} {}'.format(self.first,self.last)

class Developer(Employee): #child class
    def __init__(self,first,last,salary,prog_lang):
        #super().__init__(first,last,salary)
        Employee.__init__(self,first,last,salary) #works same as super()
        self.prog_lang=prog_lang

em1=Employee('alankar','parajuli',50000)
dev1=Developer('raknala','ilujarap',90900,'python')

print(isinstance(Developer,Employee))
print(issubclass(Developer,Employee))
print(isinstance(dev1,Developer))
#print(dev1.prog_lang)
#print(em1.fullName())
#print(dev1.fullName())
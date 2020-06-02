class Employee:

    pay_raise = 1.5 #this is a class variable
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def payRaise(self):
        self.pay=self.pay*self.pay_raise

e1=Employee('alankar','parajuli',5000)
print(e1.pay)
e1.pay_raise=1.8
e1.payRaise()
print(e1.pay)
print(Employee.pay_raise)
print(e1.pay_raise)
#print(Employee.pay_raise)
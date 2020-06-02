class Employee:
    def __init__(self,first,last,salary):
        self.first=first
        self.last = last
        self.salary=salary
    @classmethod
    def from_string(cls,emp_str):
        first , last , salary = emp_str.split('-')
        return cls(first , last ,salary)

emp1_str='alankar-parajuli-50000'

new_emp=Employee.from_string(emp1_str)
print(new_emp.first)
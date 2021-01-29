class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first + '.' + last + '@gmail.com'

    def fullname(self):
        return (f'{self.first}{self.last}\n{self.email}\nReceives:{self.pay}')

emp_1= Employee('Zareh','Kasparian',5000)
emp_2 = Employee('Marina','Kasparian',60000)



print(Employee.fullname(emp_1))
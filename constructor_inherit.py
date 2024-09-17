class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print("Name = ",self.name)
        print("ID = ",self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        super().__init__(name, idnumber)
        self.salary=salary
        self.post=post
    def display(self):
        super().display()
        print("Salary = ",self.salary)
        print("Post = ",self.post)
emp_name=input("Enter your name = ")
emp_id=int(input("Enter your ID  = "))
emp_sal=int(input("Enter your salary = "))
emp_post=input("Enter your post = ")
e1=Employee(emp_name,emp_id,emp_sal,emp_post)
e1.display()

emp_name=input("Enter your name = ")
emp_id=int(input("Enter your ID  = "))
p1=Person(emp_name,emp_id)
p1.display()

# output
# Enter your name = ajay
# Enter your ID  = 123
# Enter your salary = 300000
# Enter your post = Developer
# Name =  ajay
# ID =  123
# Salary =  300000
# Post =  Developer
# Enter your name = Pooja
# Enter your ID  = 567
# Name =  Pooja
# ID =  567
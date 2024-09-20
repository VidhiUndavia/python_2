class Person:
    name=""
    def __init__(self,name):
        self.name=name
        print("Person class constructor called")
    def display(self):
        print("Name = ",self.name)

class Student(Person):
    rollno=0
    def __init__(self, name,rollno):
        super().__init__(name)
        self.rollno=rollno
        print("Student class constructor called")
    def display(self):
        super().display()
        print("Rollno = ",self.rollno)
    
class Teacher(Person):
    subject=""
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject
        print("Teacher class constructor called")
    def display(self):
        super().display()
        print("Subject = ",self.subject)
stud=Student("Pooja",101)
stud.display()

t1=Teacher("Pratiksha","Python")
t1.display()
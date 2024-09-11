class Student:
    College="Gyanmanjari Institute"
    def __init__(self,rollno,name):
        self.roll=rollno
        self.name=name
        print("Constructor called...")
    def display(self):
        print("College = ",self.College)
        print("Roll No. = ",self.roll)
        print("Name = ",self.name)
        
stud1=Student(101,"Pooja")
roll=int(input("Enter the roll no = "))
name=input("Enter the name = ")
stud2=Student(roll,name)
stud1.display()
print("---------------------------------------")
stud2.display()
        
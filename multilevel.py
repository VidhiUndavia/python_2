class Parents:
    name=""
    def __init__(self,name):
        self.name=name
        print("Parents constructor called...")
    def display(self):
        print("Name = ",self.name)
class Child(Parents):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
        print("Child class constructor called....")
    def getAge(self):
        print("Age = ",self.age)
class Grand_child(Child):
    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address=address
        print("Grand child class constructor called....")
    def getAddress(self):
        print("Address = ",self.address)
name=input("Enter your name = ")
age=int(input("Enter your age = "))
address=input("Enter your address = ")
g1=Grand_child(name,age,address)
g1.display()
g1.getAge()
g1.getAddress()
print("------------------------")
c1=Child(name,age)
c1.display()
c1.getAge()
print("--------------------------")
p1=Parents(name)
p1.display()


# output
# D:\python_2>py multilevel.py
# Enter your name = puuja
# Enter your age = 18
# Enter your address = bhavnagar
# Parents constructor called...
# Child class constructor called....
# Grand child class constructor called....
# Name =  puuja
# Age =  18
# Address =  bhavnagar
# ------------------------
# Parents constructor called...
# Child class constructor called....
# Name =  puuja
# Age =  18
# --------------------------
# Parents constructor called...
# Name =  puuja

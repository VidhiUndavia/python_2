class Person:
    def walk(self):
        print("Person can walk")
    def talk(self):
        print("Person can talk")
class Student(Person): 
    def read(self):
        print("Student can read")
    def write(self):
        print("student can write")
    def whatIcando(self):
        super().walk()
        super().talk()
        self.read()
        self.write()
p1=Person()
p1.walk()
p1.talk()
s1=Student()
s1.read()
s1.write()
s1.whatIcando()
s1.walk()


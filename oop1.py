class Animal:
    name="0"
    def eat(self,name):
        print(name," can eat.")
        print(self.name," can eat")
        self.name=name
        print(self.name," can eat")
    def sleep(self):
        print(self.name," can sleep")
    
Tiger=Animal()
Tiger.eat("Tiger")
Tiger.sleep()
Lion=Animal()
Lion.eat("Lion")
Lion.sleep()

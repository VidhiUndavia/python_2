class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
obj = Human()
# Call the method
obj.sayHello()
# Call the method with a parameter
obj.sayHello('The EasyLearn Academy')
# output
# Hello 
# Hello The EasyLearn Academy
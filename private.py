class bank:
    def __init__(self,name,acctype,balance):
        self.name=name
        self.acctype=acctype
        self.__balance=balance
    def display(self):
        print(acc.name)
        print(acc.acctype)
        print(acc.__balance)

acc=bank("pooja","current",1000)
print(acc.name)
print(acc.acctype)
# print(acc.__balance)
acc.__balance=5000
print(acc.__balance)
acc.display()

# output
# pooja
# current
# 5000
# pooja
# current
# 1000
    
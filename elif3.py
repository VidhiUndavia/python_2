num1=int(input("Enter first number = "))
num2=int(input("Enter second number = "))

print("-----------------Menu-----------------\n1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\n")
print("Number1 = ",num1)
print("Number2 = ",num2)

choice=int(input("Enter your choice : "))

if choice==1:
    ans=num1+num2
    print("Addition = ",ans)
elif choice==2:
    ans=num1-num2
    print("Subtraction = ",ans)
elif choice==3:
    ans=num1*num2
    print("Multiplication = ",ans)
elif choice==4:
    ans=num1/num2
    print("Division = ",ans)
else:
    print("invalid choice")

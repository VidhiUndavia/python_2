#wap to find out which number is maximum in given 3 numbers
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))

if num1>num2:
    if num1>num3:
        print("First number is gratest")
    else:
        print("Third number is gratest")
else:
    if num2>num3:
        print("Second number is gratest")
    else:
         print("Third number is gratest")

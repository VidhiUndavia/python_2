def calculation(a,b):
    add=a+b
    sub=a-b
    return add,sub
num1=int(input("Enter 1st number = "))
num2=int(input("Enter 2nd number = "))
ans=calculation(num1,num2)
print(ans)
add=ans[0]
sub=ans[1]
print(add)
print(sub)

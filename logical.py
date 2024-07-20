# write a programm to find out weather the person's nationality is indian or something else.
nationality=int(input("enter nationality "))
age=int(input("enter age "))

print("AND = ",(nationality==1)and(age>=18))
print("OR = ",(nationality==1)or(age>=18))
print("OR = ",not((nationality==1)or(age>=18)))

str="The easy learn academy"
print(str)

print(str.upper())
print(str.lower())
str1="PUJA"
print(str1.isupper())
print(str.title())
print(str.istitle())
print(str.islower())

str="hello123"
print(str.isalnum())
print(str1.isalpha())
# str="123"
print(str.isnumeric())
str="  hi  "
print(str.isspace())
str="The easy learn academy"
print(len(str))
fruit1=["strawberry","pineapple","pineapple","orange"]
s=" "

print(s.join(fruit1))

python={"name":"Python","price":4500,"duration":90}
print(s.join(python))

touple2=("99","MCA","99.99","gurukul")
print(s.join(touple2))

animal={"Dog","Cow","Cat","ret"}
print(s.join(animal))

sentance="Good morning, this morning is full of sunlight and happiness, have a great morning"
print("Original = ",sentance)
print("New = ",sentance.replace("morning","night"))

print("New = ",sentance.replace("morning","night",2))

s=','
name="Theeasylearnacademy"
list1=name.split(s)
print(list1)
import sys
list1=[0,'b','a']
for item in list1:

    try:
        print("Entry = ",item)
        ans=1/int(item)
        
    except :
        print(sys.exc_info()[0])
        print("Error occured")
print("bye")

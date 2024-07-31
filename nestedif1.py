birthdayFlag=int(input("Today is the birthday of the person? "))


if birthdayFlag==1:
    print("Yes today is the birthday of the person")
    partyflag=int(input("There is party or not? "))
    if partyflag==1:
        print("Yes let's go for the party")
    else:
        print("No there is not any kind of plan for the party")  
else:
    print("No there is no any kind of event today")

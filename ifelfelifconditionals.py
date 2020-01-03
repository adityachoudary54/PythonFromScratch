list1=[1,4,2,3]
x=int(input("Enter a no:").strip())
if x in list1:
    print("{} is in the list".format(x))
else:
    print("{} is not in the list".format(x))
#in,not in are the keywords can be used
age=int(input("Enter the age:").strip())
if age>18 and age<=100:
    print("You can drive")
elif age==18:
    print("You have to come to driving center to check whether u can drive or not")
elif age>=7 and age<18:
    print("You can't drive")
else:
    print("Invalid input")

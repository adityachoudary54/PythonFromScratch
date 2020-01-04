print('Welcome to loops')
items={int,float,'harry',5,3,4,2,1,3,5,6,24}
for item in items:
    if type(item)==type(6) and item>2:
        print(item)

i=0
while True:
    if i+1<5:
        i+=1
        continue
    print(i+1,end=" ")
    if i==20:
        break
    i+=1
while True:
    inp=int(input("Enter a number:"))
    if inp>100:
        print("You have entered a number greater than 100")
        break
    else:
        print("Try Again")


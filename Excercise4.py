while True:
    n=int(input("Enter a number:"))
    state=bool(input("Enter state(0/1):").strip()=='1')
    print(n,state)
    print("The req pattern is->")
    if state==True:
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print("")
    else:
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            print("")
    ch=input("Do you want to continue(Y/N):")
    if ch.lower()!="y":
        print('Thanks for using')
        break
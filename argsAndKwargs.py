def funArgs(*args):
    print(args[0])
    print(type(args))
lst=["harry",'aloo','pyaz','sabzi','tinde']
funArgs(*lst)
#first normal argument
# then args
# then kwargs

def myFunc(normalArg,*args,**kwargs):
    print(normalArg)
    for item in args:
        print(item)
    for item in kwargs.items():
        print(item)
book={'adi':"intelligent","rukmini":"chural"}
myFunc(45,*lst,**book)
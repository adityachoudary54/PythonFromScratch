d={}
while True:
    x=input("Enter key value pair seperated by comma:")
    if x!='end':
        l=x.split(",")
        d[l[0]]=l[1]
    else:
        break
print(input("what is ur name:"))
print(d)
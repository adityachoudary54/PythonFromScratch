# operator=input('Enter the operator:').strip()
# a,b=int(input('Enter no. 1:').strip()),int(input('Enter no. 2:').strip())
def myPartition(s):
    if '+' in s:
        return s.partition('+')
    elif '-' in s:
        return s.partition('-')
    elif '**' in s:
        return s.partition('**')    
    elif '*' in s:
        return s.partition('*')
    elif '/' in s:
        return s.partition('/')
    elif '%' in s:
        return s.partition('%')    
    else:
        return -1,-1,-1
a,operator,b=myPartition(input("Enter the expression to be evaluated:"))
# print(a,"  ",operator,"  ",b)
a=int(a)
b=int(b)
if operator=='*':
    if (a==45 and b==3) or (a==3 and b==45):
        print(555)
    else:
        print(a*b)
elif operator=="+":
    if (a==56 and b==9) or (a==9 and b==56):
        print(77)
    else:
        print(a+b)
elif operator=='/':
    if (a==56 and b==6):
        print(4)
    else:
        print(a//b)
else:
    if operator == '-':
        print(a-b)
    elif operator == '%':
        print(a%b)
    elif operator == '**':
        print(a**b)
    else:
        print("Wrong operator")
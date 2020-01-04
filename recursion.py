def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
# print(fact(int(input("Enter a number:"))))
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(int(input("Enter a number:"))))
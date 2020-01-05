num_lis=[1,2,3,4,5,6]
x=list(map(lambda x:x**2,num_lis))
print(x)

numbers=["3","34","64"]
print(numbers)
numbers=list(map(int,numbers))
print(numbers)

def square(a):
    return a*a
def cube(a):
    return a**3
func=[square,cube]
for i in range(5):
    val=list(map(lambda x: x(i),func))
    print(val)

# filter function
list_1=[1,2,3,4,5,6,7,8,9]
div_2=list(filter(lambda x: x%2==0,list_1))
print(div_2)

# Reduce function
from functools import reduce
list1=[1,2,3,4,7]
num=reduce(lambda x,y: x+y,list1)
print(num)


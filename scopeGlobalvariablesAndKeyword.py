# l=10
# def func(n):
#     # l=5
#     m=8
#     m+=2
#     global l
#     l+=1
#     print(l,m)
#     print(n)
# func(20)
# print(l)
x=89
def func1():
    x=20
    def rohan():
        global x
        x=88
    print("Before calling rohan():",x)
    rohan()
    print("After calling rohan():",x)
func1()
print(x)
# def funcRet(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=funcRet(int(input()))
# print(a)

# def executor(func):
#     func("this")
# executor(print)

# decorators

def dec1(func1):
    def nowExec():
        print("Executing now")
        func1()
        print("Executed")
    return nowExec

@dec1
def who_is_adi():
    print("Adi does Wonderfull things")
# who_is_adi=dec1(who_is_adi)
who_is_adi()
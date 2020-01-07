class A:
    classvarA="I am a class variable in class A"
    def __init__(self):
        self.var='I am in class A constructor'
        self.classvarA='I am instance var of class A'
        self.special='special'
class B(A):
    # Instance variable of class A would be prefered
    classvarA="I am in class B"
    def __init__(self):
        super().__init__()
        self.var='I am in class B constructor'
        self.classvarA='I am instance var of class B'
        print(super().classvarA)
""" 
First instance variable is searched 
then class variable is searched
"""
a=A()
b=B()
# print(b.classvarA)
# print(b.special)

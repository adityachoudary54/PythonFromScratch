class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        if self.fname==None or self.lname==None:
            return "Email isnt set"
        return f"This Employee is {self.fname} {self.lname}"
    #setter
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email isnt set"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        # self.fname=names.split('.')[0]
        # self.lname=names.split('.')[1]
        self.fname,self.lname=names.split('.')
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        print('Deleter worked fine')

#Object Introspection
"""
Getting to know about the details of the object, their type,their class, how its stored etc.
"""
skillf=Employee("Skill","F")
print(skillf.email)
print(type(skillf))
print(id(skillf))
o="This is a string"
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
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
x=Employee('hindustani','lakhan')
y=Employee('jat','world')
print(x.explain(),f"\n{x.email}")
x.email="adi.choudhary@gmail.com"
print(x.explain(),f"\n{x.email}")
del x.email
print(x.explain(),f"\n{x.email}")

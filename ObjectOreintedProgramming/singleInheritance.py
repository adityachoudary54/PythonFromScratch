class Employee:
    no_of_leaves=8
    def printDetails(self):
        return f"Name is:{self.name}.\nSalary is:{self.salary}.\nRole is:{self.role}."
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves=leaves
    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    
class Programmer(Employee):
    def __init__(self, name, salary, role,lang):
        # super().__init__(name, salary, role)
        self.name=name
        self.salary=salary
        self.role=role
        self.lang=lang
    def printProgrammerDetails(self):
        return f"Programmer name is:{self.name}.\nSalary is:{self.salary}.\nRole is:{self.role}.\nLanguage is:{self.lang}"
yoyo=Programmer.from_str("yoyo-56000-Doctor-{}".format(['C++','Python','Java']))
print(yoyo.printProgrammerDetails())
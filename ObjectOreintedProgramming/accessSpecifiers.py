class Employee:
    no_of_leaves=8
    _protectedVariable=10
    __privateVariable=20
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
    @staticmethod
    def printGood(string):
        print(f"This is good {string}")
print(Employee._protectedVariable)
print(Employee._Employee__privateVariable)
print(Employee.__dict__)

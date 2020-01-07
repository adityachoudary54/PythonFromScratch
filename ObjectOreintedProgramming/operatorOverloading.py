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
    @staticmethod
    def printGood(string):
        print(f"This is good {string}")
    # Dunder methods
    def __add__(self,other):
        return int(self.salary)+int(other.salary)
    def __truediv__(self,other):
        return int(self.salary)/int(other.salary)
    def __repr__(self):
        return self.printDetails()
    # str is prefered over repr
    def __str__(self):
        return f"{self.name},{self.salary},{self.role}."
emp1=Employee.from_str("karan-455-manager")  
emp2=Employee.from_str("arjun-275-manager")  
print(emp1+emp2)
print(emp1)
# If str isnt present then repr is shown on calling emp1.__str__()
print(emp1.__repr__())
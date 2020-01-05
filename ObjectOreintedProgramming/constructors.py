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

# harry=Employee()
# harry.name="Aditya"
# harry.salary=350000
# harry.role="Manager"
# rohan=Employee()
# rohan.name="Rohan"
# rohan.salary=85000
# rohan.role="Employee"
amul=Employee("Amulya",56000,"Doctor")
# amul.change_leaves(int(input(f"Enter the no. of leaves of {amul.name}")))
print(amul.printDetails())
Employee.change_leaves(28)
print(amul.no_of_leaves)
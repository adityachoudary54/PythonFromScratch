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

class Player:
    no_of_games=4
    def __init__(self,name,game):
        # super().__init__()
        self.game=game
        self.name=name
    def printDetails(self):
        return f"The name is {self.name}, game is {self.game}"

class coolProgrammer(Employee,Player):
    language='C++'
    def printLanguage(self):
        print(self.language)

shubham=Player("shubham",['rugby','cricket'])
karan=coolProgrammer("Karan",8999,'CoolProgrammer')
print(karan.printDetails())
karan.printLanguage()
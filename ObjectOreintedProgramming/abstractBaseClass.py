from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0
class Rectangle(Shape):
    type="rectangle"
    sides=4
    def __init__(self,length,breadth):
        # super().__init__()
        self.length=length
        self.breadth=breadth
    def printArea(self):
        return self.length*self.breadth
rec=Rectangle(5,6)
print(rec.printArea())
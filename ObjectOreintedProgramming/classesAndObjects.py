class Student:
    no_of_leaves=10#Same for all class objects
harry=Student()
harry.name="aditya"
harry.std=8
larry=Student()
larry.name="Hello world"
print(harry.name,larry.name)
print(harry.no_of_leaves,larry.no_of_leaves)
Student.no_of_leaves=7#Such variables can be changed through class only
print(harry.no_of_leaves,larry.no_of_leaves)
print(harry.__dict__)
print(Student.__dict__)
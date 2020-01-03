"""
List methods
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
"""
myList=[2,5,3,4,1,6,7,1,9,0]
myList.append("hello")
print(myList)
print(myList.clear())
myList=[2,5,3,4,1,6,7,1,9,0]
print(myList.copy())
print(myList.count(3))
myList.extend([1,2,3,4])
print(myList)
print(myList.index(3))
myList.insert(1,"hello")
print(myList)
myList.pop(1)#removes taking index as arg
print(myList)
myList.remove(6)#removes first accurence of actual element
print(myList)
myList.reverse()
print(myList)
myList.sort()
print(myList)

# slicing
"""same as in strings just keep in mid for negative slicing dont use number less that 1"""

# lists-"immutable"
# tupple-"non-immutable"

# swapping
a=7
b=2
a,b=b,a
print(a,b)
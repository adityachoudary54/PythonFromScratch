"""
Iterable- __iter__ or __getitem__() is defined
Iterator- __next__()
Iteration- 
"""
# range is a generator

# Creating ur own generator
def gen(n):
    for i in range(n):
        yield i
g=gen(10)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in g:
    print(f"in loop {i}")

h="harry"
itr=iter(h)
print(itr.__next__())
for c in h:
    print(c)

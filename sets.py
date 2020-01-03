"""
Set methods
union
add
intersection
difference
update
remove
"""
s=set()
print(type(s))
s_from_list=set([1,1,1,2,2,2,3,3,4,4,4,4,8,8,6,6,6])
print(s_from_list)
s.add(1)
print(s)
s1=s.intersection({1,2})
print(s1,"s1")
s1={4,5}
print(s.isdisjoint(s1))
print(s1)
s1.remove(5)
print(s1)


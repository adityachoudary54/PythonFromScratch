d={"harry":"Burger",
"Rohan":"Fish","Skillf":"Roti",
"Shubham":{"B":"maggie","L":"roti","D":"Chicken"}}
d['Aditya']="Junk Food"
print(d["Aditya"])
print(d["Shubham"])
d[420]='kebabs'
print(d)
del d[420]
print(d)
# .copy function should be used to create a copy otherwise original items would also get affected by the changes of copy
# eg
a={"harry":"Burger",
"Rohan":"Fish","Skillf":"Roti"}
b=a
c=a.copy()
del b["harry"]
del c["Rohan"]
print(a,"\n",b,"\n",c)#Harry is removed from a but Rohan isn't
"""dictionary methods 
clear
copy
get
fromkeys
items
keys
pop
popitem-Removes the last inserted key-value pair
setdefault-	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update
values
"""
print(d.keys())
print(d.items())
print(d.values())
d.update({"Rohan":"bangen"})
print(d)
a=(1,2,3)
b=0
print(dict.fromkeys(a,b))

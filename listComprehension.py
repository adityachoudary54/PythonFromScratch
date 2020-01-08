ls=[i for i in range(100) if i%3==0]
print(ls)

dict1={i:f"item{i}" for i in range(100) if i%6==0}
rev_dict1={x:y for y,x in dict1.items()}
print(dict1)
print(rev_dict1)

dresses={dress for dress in ['dress1','dress2','dress3','dress4','dress1','dress2','dress3','dress4','dress1','dress2','dress3','dress4','dress1','dress2','dress3','dress4']}
print(dresses)

#generator comprehsnion, generators can be iterated only once
evens=(i for i in range(100) if i%2==0)
print(type(evens))


myStr=" aditya choudhary 36.8  "
print(len(myStr))
print(myStr[0:8:2])
print(myStr[::-1])
print(myStr.isalnum())
"""
isalnum
endswith
count
capitalize
lower
upper
replace
format
index
isalpha
isdecimal
isdigit
join
partition
split
startswith
strip
"""
print(myStr.endswith("hary"))
print(myStr.count("a"))
print(myStr.capitalize())
print(myStr.lower())
print(myStr.upper())
print(myStr.replace("choudhary","jaat"))

print("for only {price:.2f} dollars".format(price=36.827))
print(myStr.index("chou"))
print(myStr.isalpha())
print(myStr.isdecimal())
print(myStr.isdigit())
myTuple = ("John", "Peter", "Vicky")
print("#".join(myTuple))
# Search for the word "chou", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
print(myStr.partition("chou"))
print(myStr.split(" "))
print(myStr.startswith("adi"))
print(myStr.strip())#removes spaces from the beginning and the end of a string

print(input("Enter a string:").strip(' ').replace(' ',''))
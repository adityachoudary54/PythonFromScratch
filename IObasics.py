"""
"r"- open file for reading-default
"w"- open file for writing
"x"- creates file if doesn't exists
"a"- add more conntent to file
"t"- text mode-default
"b"- binary mode
"+"- read and write mode(used for updating)
"""

# # Writing to a file
# f=open("inputfile.txt","a")
# #It overwrites the previous wrtten content
# a=f.write("Coding is fun and u should always do it.") 
# print(a)
# f.close()


# # Reading from a files
f=open("inputfile.txt","rt")
# #Using readlines() to create a list of lines
print(f.readlines())
# # # Using readline function
# # print(f.readline())
# # print(f.readline())
# # # for reading lines
for line in f:
    print(line,end="")
# # content=f.read(3)#reads the whole doc else reads the no. of characters specified
# # print(content)
# # content=f.read(3)
# # print(content)
f.close()

#handle read and write both
# f=open("inputfile.txt","r+")
# print(f.read())
# f.write("Thanks")
# f.seek(0,0)#offset and whence(imp)
# # whence
# # 0 - absolute positioning
# # 1 - relative to current position
# # 2 - relative to file's end
# print(f.read())

# # More details on python files
# f=open("inputfile.txt","r+")
# # print(f.tell())
# print(f.readline())
# # print(f.tell())
# f.seek(10)
# print(f.readline())
# # print(f.tell())
# f.close()

#Using with block
# with open("inputfile.txt","r+") as f:
#     a=f.read(4)
#     print(a)
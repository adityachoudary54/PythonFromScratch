f1=open("inputfile.txt")
try:
    f2=open("does.txt")
except EOFError as e:
    print("End of file aagyi bhai")
except IOError as e:
    print("IO error aagyi bhai")
except Exception as e:
    print(e)
else:
    print("This will run only when except isnt running")
finally:
    print("Run this anyway")
    f1.close()
    # f2.close()
print("This is the important stuff")
# Health management system
# 3 clients - Harry, Rohan and Hammad
# total 6 files
def getdate():
    import datetime
    return datetime.datetime.now()
print(getdate())
# with open("HealthManagementSystem/testFile.txt","w+") as f:
#     f.write("This is a test file and you can do anything with it.")

# with open("HealthManagementSystem/names.txt","w+") as f:
#     name=input("Enter the name of the person:")
#     f.write(name+'\n')
# print(name)

while True:
    print("Enter 0 to enter data")
    print("Enter 1 to access existing data")
    print("Enter 2 to update existing data")
    ch=int(input("Enter your choice(0/1/2):"))
    if ch==0:
        print("Enter the details asked ->")
        with open("HealthManagementSystem/names.txt","a+") as f:
            name=input("Enter the name of the person:")
            f.write(name+'\n')
        with open("HealthManagementSystem/{}Diet.txt".format((name).lower()),"a+") as f:
            diet=input("Enter the diet of the person:")
            f.write(diet+'\n')
        with open("HealthManagementSystem/{}Exercise.txt".format((name).lower()),"a+") as f:
            exercise=input("Enter the excercise routine of the person:")
            f.write(exercise+'\n')
    elif ch==1:
        names_dict={}
        with open("HealthManagementSystem/names.txt","r+") as f:
            list_names=f.readlines()
            search_name=[]
            for item in list_names:
                print(item)
                search_name.append(item.lower())
        ch_name=input("Enter the name whose data is to be accessed").strip()
        # print(ch_name+'\\n')
        # print(search_name)
        if ch_name.lower()+'\n' in search_name:
            # print("fine")
            with open("HealthManagementSystem/{}Diet.txt".format(ch_name.lower(),"r+")) as f:
                content=f.read()
                print(content)
            with open("HealthManagementSystem/{}Exercise.txt".format(ch_name.lower()),"r+") as f:
                content=f.read()
                print(content)
    elif ch==2:
        pass
    ch_prgrm=input("Do you want to enter again?(Y/N):").strip().lower()
    if(ch_prgrm!='y'):
        break


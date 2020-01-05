import time
# initial=time.time()
# i=0
# while i<45:
#     print(i)
#     i+=1
# ts1=time.time()
# print("While loop ran in :{}".format(ts1-initial))
# for i in range(45):
#     print("for loop {}".format(i))
# print("for loop ran in :{}".format(time.time()-ts1))
localTime=time.asctime(time.localtime(time.time()))
print(localTime)
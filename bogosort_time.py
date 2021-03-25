import random as random
import time as time
import matplotlib.pyplot as plt


#Bogosort algorithmus
def bogosort(list):
    fails = 0
    while not check(list):
        print(list)
        random.shuffle(list)
        fails += 1
    print("Success! Your sorted list is:\n",list,"\n with ", fails, " fails")

#überprüft ob Liste bereits sortiert ist
def check(list):
    for i in range(len(list)):
        if i+1 < len(list):
            if list[i] <= list[i+1] :
                print(list[i],list[i+1])
                continue
            else:
                return False
    return True


#data = [3,2,2,1,7,8]
#bogosort(data)


times = []
for i in range(9):
    totaltime = 0
    for j in range(5):
        starttime = time.time()
        testdata=[i-n for n in range(i)]
        bogosort(testdata)
        totaltime += time.time()-starttime
        testdata=[i-n for n in range(i)]
    times.append(totaltime/5)

plt.plot(times, marker='D')
plt.ylabel("Laufzeit")
plt.xlabel("n")
plt.show()

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
    return fails

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


failslist = []
for i in range(8):
    testdata=[i-n for n in range(i)]
    a=[]
    for j in range(5):
        a.append(bogosort(testdata))
        testdata=[i-n for n in range(i)]
    failslist.append(sum(a)/len(a))

plt.plot(failslist, marker='D')
plt.ylabel("Laufzeit")
plt.xlabel("n")
plt.show()

import random

#Bogosort algorithmus
def bogosort(list):
    fails = 0
    while not check(list):
        print(list)
        random.shuffle(list)
        fails += 1
    print("Fertig! Die sortierte Liste ist:\n",list,"\n mit ", fails, " Mischvorgängen")

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

data = []
length = int(input("Welche groß ist deine Liste?"))

for i in range(length):
    elmnt = input("Gebe bitte eine Listenelement ein:")
    data.append(elmnt)
    

bogosort(data)

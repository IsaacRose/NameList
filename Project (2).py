import random
def namelist():
    names=[]
    rand=random.randrange(0,10)
    print (rand)
    count=0
    while count != rand:
        nameinput=input("Add names: ")
        if nameinput=="Isaac":
            print ("hey")
        names.append(nameinput)
        count=count+1
    print (names)

namelist()    

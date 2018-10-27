def isconsecutive(l):
    for i in range(len(l)-3):
        c=[l[i] for j in range(4)]
        #print(c)
        if(l[i:i+4]==c[0:4]):
            return True
    return False

listitem=input("Enter list element")
li=listitem.split()
print(isconsecutive(li))
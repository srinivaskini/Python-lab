fname=input("Enter a file name : ")
f=open(fname,"r")
total=0
c=0
for l in f:
    scores=l.split()
    for s in scores:
        c+=1
        total+=int(s)
print("Total : ",total)
print("Average : ",total/c)
def indexOfSmallestElement(l):
    min=0
    l=list(map(int,l))
    for i in range(1,len(l)):
        if l[i]<l[min]:
            min=i
    return min

lst=input("Enter a list of integers : ")
lst=lst.split()
print("Smallest index : ",indexOfSmallestElement(lst)+1)
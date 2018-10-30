str=input("Enter array elements in sorted order ")
key=int(input("Enter key"))
l=list(map(int,str.split()))
print(l)
low=0
high=len(l)-1
f=0
while low<=high:
    mid=(low+high)//2
    if l[mid]==key:
        f=1
        break
    elif key<l[mid]:
        high=mid-1
    else:
        low=mid+1
if f==0:
    print("Element not found")
else:
    print("Element found at index :",mid)

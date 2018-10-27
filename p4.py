a=0
b=1
n=int(input("Enter number of terms :"))
print(a,b,end=' ')
for i in range(n-2):
    r=a+b
    a=b
    b=r
    print(r,end=' ')
    
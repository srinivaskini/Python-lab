str=input("Enter string : ")
c=0
for s in str:
    if s.isupper():
        c+=1
print("No of capital letters in a given string is : ",c)
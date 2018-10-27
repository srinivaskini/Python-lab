str=input("Enter string")
new_str=''
for i in range(len(str)-1,-1,-1):
    new_str+=str[i]
if(str==new_str):
    print("Palindrome !!!")
else:
    print("Not a palindrome !!!")
#alternate---t=str[::-1]
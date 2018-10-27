count = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0 }
str=input("Enter string")
for s in str:
    if(s in count):
        count[s]+=1
    
for c in count:
    if(count[c]!=0):
        print(c,"-->",count[c])
        
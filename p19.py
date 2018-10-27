fname=input("Enter a file name : ")
f=open(fname,"r")
chr=0
words=0
lines=0
for l in f:
    lines+=1
    wordlist=l.split()
    words+=len(wordlist)
    chr+=len(l)
print("characters :",chr)
print("Words : ",words)
print("Lines : ",lines)
            
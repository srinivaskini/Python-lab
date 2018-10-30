str1=input("Enter string 1 : ")
str2=input("Enter string 2 : ")
str=str1+str2
final_word=''
for w in str:
    if(w.isupper()):
        final_word+=w
print("Final word : "+final_word)
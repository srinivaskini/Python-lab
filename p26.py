import threading
class palindrome(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.str=s
    def run(self):
        t=''
        for i in range(len(self.str)-1,-1,-1):
            t+=self.str[i]
        if(t==self.str):
            print("Its a palindrome")
        else:
            print("Its not a palindrome")
class vowel(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.str=s
    def run(self):
        c=0
        for i in self.str:
            if i in ('a','e','i','o','u'):
                c+=1
        print("No of vowels : ",c)
        
str=input("Enter string")
t1=palindrome(str)
t2=vowel(str)
t1.start()
t2.start()     
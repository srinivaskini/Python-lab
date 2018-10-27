def func(str):
    newstr=''
    for s in str:
        if s not in "!()-[]{};:''',\,<>/?@#$%^&*_~":
            newstr+=s
    return newstr

str=input("Enter input : ")   
print(func(str))
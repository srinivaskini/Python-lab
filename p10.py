def generate(n):
    n_dict=dict()
    for i in range(1,n+1):
        n_dict[i]=i*i
    return n_dict

n=int(input("Enter n : "))
print("Dictionary is : ",generate(n))
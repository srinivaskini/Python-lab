student={'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}
sorted_list=sorted(student,key=student.get,reverse=True)
total=0
for i in student:
    total+=student[i]
avg=total/len(sorted_list)
print("Top three scorers :",sorted_list[:3])
print("Average is : ",avg)
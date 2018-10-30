key = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'] 
student_answers = [ ['C', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'] ,['A' ,'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'], ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'], ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'], ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'], ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'], ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'], ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'], ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'] ]
j=1
for sm in student_answers:
    score=0
    for i in range(10):
        if(sm[i]==key[i]):
            score+=1
    print("Student ",j," : ",score)
    j+=1
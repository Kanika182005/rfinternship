Marks = [78, 85, 90, 67, 85, 92, 78]
count = 0 
grades = []
 # calculate average
Avg = sum(Marks)/ len(Marks)
print("Average of marks is:",Avg)

#calculate highest and lowest
Max = max(Marks)
Min = min(Marks)
print ("Highest and Lowest marks are:", Max, Min)

#count how many students scored above average
for i in Marks:
    if i > Avg:
        count+=1
print ("Total students who scored above Average are:", count)        

#create grade distribution
print("--------Grade distribution------- ")
for i in Marks:
    if i >=90:
        print("Grade for ",i ,"is A")
        grades.append("A")
    elif i>=80 and i< 90:
        print("Grade for ",i ,"is B")
        grades.append("B")
    elif i >=70 and i<80:
        print("Grade for ",i ,"is C")
        grades.append("C")
    elif i>=60 and i<70:
        print("Grade for ",i ,"is D")
        grades.append("D")    
    else :
        print("Grade for ",i ,"is F")
        grades.append("F")
print ("Marks are :", Marks)        
print(" Grades are:", grades)        
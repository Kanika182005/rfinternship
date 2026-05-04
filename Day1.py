data = [10, None, 20, 10 ," ", 30 , None , 40]
print(data)
removed= []
clean = []

#remove invalid values
for i in data :
    if i == None or i == " ":
        removed.append(i)
    else :
        clean.append(i)
print("list containing invalid values are:", removed)
print("list containing valid values are:", clean)

# remove duplicates
unique = []
for i in clean:
    if i not in unique:
        unique.append(i)
    else:
        removed.append(i)
print("unique list is:", unique) 
print("Final removed elements are:", removed)

#return clean list
print("clean list is:", unique)

# count how many values were removed
print("Total removed elements are:", len(removed)) 

#sort final list
print("Final sorted list is:", unique.sort())
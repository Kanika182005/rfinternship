import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# list of dictionaries
data = [
    {"name" :"Amit", "age" : 20, "marks": 85 },
    {"name": "Riya", "age" : 21, "marks":90 }

]
print (data)

# calculate average value and hadle missing values
total =0

for i in data:
    if "marks" in i and i["marks"] not in [None, ""]:
        total= total+ i["marks"]
Avg = total/len(data)
print ("Average marks is:", Avg)
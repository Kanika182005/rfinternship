with open("students.csv", "r") as file:
    lines = file.readlines()

headers = lines[0].strip().split(",")

students = []

for line in lines[1:]:
    values = line.strip().split(",")

    # Missing values handle
    age = int(values[1]) if values[1] != "" else 0
    marks = int(values[2]) if values[2] != "" else 0

    student = {
        "NAME": values[0],
        "AGE": age,
        "MARKS": marks
    }

    students.append(student)

print(students)
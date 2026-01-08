#Number of students
n=int(input("Enter number of students:"))
students=[]

#input details of students
for i in range(n):
    print(f"\nStudent {i+1}")
    name=input("Enter name:")
    score=int(input("Enter score(0-100):"))

    students.append({"name":name,"score":score})

    #average score
    total=0
    for s in students:
        total+=s["score"]

        average=total/n

#Highest and Lowest score
highest=students[0]
lowest=students[0]

for s in students:
    if s["score"] > highest["score"]:
        highest=s
    if s["score"] < lowest["score"]:
        lowest=s

#passed students
passed_students=[]
for s in students:
    if s["score"] >=40:
        passed_students.append(s["name"])

#Grade function
def get_grade(score):
    if score >=90:
        return "A"
    elif score >=75:
        return "B"
    elif score >=60:
        return "C"
    elif score >=40:
        return "D"
    else:
        return "F"

#Publish results
print("\n------Results-------")
print("Average score:", average)
print("Highest score:", highest["score"],"-", highest["name"])
print("Lowest score", lowest["score"],"-", lowest["name"])
print("Passed students:", passed_students)

print("\nStudent Grades:")
for s in students:
    print(s["name"],":", get_grade(s["score"]))

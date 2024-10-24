stud_count = int(input("how many students does the class has? "))
grades = []
sum = 0
for i in range(0,stud_count):
    grade = int(input())
    sum += grade
    grades.append(grade)
avereage = sum / stud_count
if avereage >= 90:
    print("A")
elif avereage >=80:
    print("B")
elif avereage >=70:
    print("C")
elif avereage >=60:
    print("D")
else:
    print("F")
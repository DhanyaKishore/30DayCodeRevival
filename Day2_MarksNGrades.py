# Problem: Average and Grades of five subject marks
# Platform: HackerRank
# Date: 2025-05-31
# Author: Dhanyasree

marks=[]
for i in range(5):
  m=float(input(f"Enter mark{i+1}:"))
  marks.append(m)
avg=sum(marks)/5
 if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "Fail"
print(f"Average:{avg}\nGrade:{grade}")
  
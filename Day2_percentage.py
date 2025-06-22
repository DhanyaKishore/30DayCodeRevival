# Problem: Finding the percentage
# Platform: HackerRank
# Date: 2025-05-31
# Author: Dhanyasree

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    marks=student_marks[query_name]
    avg= sum(marks)/len(marks)
    print(f'{avg:.2f}')
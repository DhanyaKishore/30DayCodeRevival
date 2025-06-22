# Problem: Nested Lists
# Platform: HackerRank
# Date: 2025-05-31
# Author: Dhanyasree

n=int(input())
S=[]
for _ in range(n):
    name = input()
    score = float(input())
    S.append([name,score])
grade=sorted(set([score for name,score in S]))
sm=grade[1]
names=[name for name,score in S if score==sm]
for name in sorted(names):
    print(name)
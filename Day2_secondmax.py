# Problem: Find the Runner-Up Score!
# Platform: HackerRank
# Date: 2025-05-31
# Author: Dhanyasree

n = int(input())
A = list(map(int, input().split()))
max1=max2=float('-inf')
for i in range(len(A)):
    if(A[i]>max1):
        max2=max1
        max1=A[i]
    elif A[i]>max2 and A[i]!=max1:
        max2= A[i]
print(max2)
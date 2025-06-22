# Problem: List Comprehensions
# Platform: HackerRank
# Date: 2025-05-31
# Author: Dhanyasree

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lc=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(lc)
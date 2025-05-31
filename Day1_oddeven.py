# Problem: Python If-Else
# Platform: HackerRank
# Date: 2025-05-30
# Author: Dhanyasree

n=int(input())
if n%2==0 :
    if n<5:
        print("Not Weird")
    elif 5<n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
else:
    print("Weird")
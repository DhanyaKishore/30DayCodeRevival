# Problem: Operation on Lists with commands
# Platform: HackerRank
# Date: 2025-05-31
# Author: Dhanyasree

N = int(input())
arr=[]
for _ in range(N):
    com=input().strip().split()
    o=com[0]
    if o=="insert":
        i=int(com[1])
        e=int(com[2])
        arr.insert(i,e)
    elif o=="print":
        print(arr)
    elif o=="remove":
        e=int(com[1])
        arr.remove(e)
    elif o=="append":
        e=int(com[1])
        arr.append(e)
    elif o=="sort":
        arr.sort()
    elif o=="pop":
        arr.pop()
    elif o=="reverse":
        arr.reverse();
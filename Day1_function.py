# Problem: Create a Function
# Platform: HackerRank
# Date: 2025-05-30
# Author: Dhanyasree

def is_leap(year):
    leap = False
    if year%4==0 :
        if year%100==0 :
            if year%400==0:
                leap = True
        else:
            leap = True
    return leap
year = int(input())
print(is_leap(year))
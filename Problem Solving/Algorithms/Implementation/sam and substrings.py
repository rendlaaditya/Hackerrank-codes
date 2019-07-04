#!/bin/python3
def substrings(s):
    n=len(s)
    if n==1:
        return int(s)
    mainsum=0
    procsum=0
    for i in range(n):
        procsum=procsum*10+int(s[i])*(i+1)
        mainsum+=procsum
    return mainsum%(10**9+7)
s = input()
print(substrings(s))
#!/bin/python3
import math
def strangeCounter(t):
    n=math.log(t/3+1,2)
    if n%1==0:
        return 1
    return 2*3*(2**math.floor(n))-t-2
print(strangeCounter(int(input())))
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    n=len(c)
    if k==n:
        return sum(c)
    if n==1:
        return c[0]
    i=1
    total=0
    c.sort()
    while(len(c)>k):
        n=len(c)
        d=c[-k:]
        e=sum(d)
        total=total+e*i
        i=i+1
        c=c[:n-k]
    total=total+sum(c)*i
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

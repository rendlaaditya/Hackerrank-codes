#!/bin/python

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse(n):
    a=list(str(n))
    a=a[::-1]
    b=''.join(a)
    return int(b)
def beautifulDays(i, j, k):
    d=0
    for l in range(i,j+1):
        if(abs(l-reverse(l))%k==0):
            d=d+1
    return d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = raw_input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

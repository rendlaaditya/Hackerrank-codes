#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    b=[0]*101
    for i in a:
        try:
            b[i]+=1
        except:
            b[i]=1
    m=1
    for j in range(1,100):
        m=max(m,b[j]+b[j-1])
        
    return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

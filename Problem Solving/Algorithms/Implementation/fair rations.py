#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    cnt=0
    for i in B:
        if i%2!=0:
            cnt=(cnt+1)%2
    if cnt==1:
        return 'NO'
    i=0
    n=len(B)
    while(i<n):
        if B[i]%2!=0:
            if i+1<n:
                cnt+=2
                B[i]+=1
                B[i+1]+=1
        i=i+1
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

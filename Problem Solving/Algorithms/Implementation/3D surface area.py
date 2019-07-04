#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    area=0
    h,w=len(A),len(A[0])
    for i in range(h-1):
        for j in range(w-1):
            area+=abs(A[i][j]-A[i+1][j])+abs(A[i][j]-A[i][j+1])
    area+=(h-2)*(w-2)*2
    return area
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []
    A=[[0]*(W+2)]
    for _ in range(H):
        A.append([0]+list(map(int, input().rstrip().split()))+[0])
    A.append([0]*(W+2))
    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

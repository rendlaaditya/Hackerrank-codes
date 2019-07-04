#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    if(k==len(arr)):
        return max(arr)-min(arr)
    n=len(arr)
    arr.sort()
    c=10000000000
    i=0
    while(i<n and i+k-1<=n-1):
        c=min(c,arr[i+k-1]-arr[i])
        i=i+1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

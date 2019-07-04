#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + int((r - l)/2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x)
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else: 
        return l

def twoArrays(k, A, B):
    if max(A)+min(B)<k or max(B)+min(A)<k:
        return 'NO'
    if min(A)+min(B)>=k:
        return 'YES'
    A.sort()
    B.sort()
    n=len(A)
    t=binarySearch(B,0,n-1,k-A[0])
    if A[n-t]+B[t-1]<k:
        return 'NO'
    return 'YES'
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()

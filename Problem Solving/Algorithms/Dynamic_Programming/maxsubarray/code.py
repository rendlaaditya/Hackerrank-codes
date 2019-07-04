#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the maxSubarray function below.
# this returns the maximum subarray sum and maximum subsequence sum. Both were calculated in single traversal
def maxSubarray(arr):
    n=len(arr)
    if n==1:
        return arr[0],arr[0]
    bool=0
    subseq=0
    if arr[0]>=0:
        bool=1
        subseq=arr[0]
    arr2=arr[0]
    i=1
    subsum=arr2
    while(i<n):
        c=arr[i]
        arr2=max(arr2+c,c)
        subsum=max(subsum,arr2)
        if c>=0:
            bool=1
            subseq+=c
        i+=1
    if bool==0:
        subseq=max(arr)
    return subsum,subseq
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = maxSubarray(arr)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()

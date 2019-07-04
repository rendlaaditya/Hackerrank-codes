#!/bin/python

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V, arr):
    def bsearch(arr,start,end,V):
        mid=start+(end-start)/2
        if(arr[mid]==V):
            return mid
        elif(arr[mid]>V):
            return bsearch(arr,start,mid-1,V)
        else:
            return bsearch(arr,mid+1,end,V)
    start=0
    end=len(arr)-1
    t=bsearch(arr,start,end,V)
    return t
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(raw_input())

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

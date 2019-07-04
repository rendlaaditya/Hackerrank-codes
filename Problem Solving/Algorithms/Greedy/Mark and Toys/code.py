#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    if(len(prices)==1):
        if(k>=prices[0]):
            return 1
        else:
            return 0
    if(min(prices)>k):
        return 0
    if(sum(prices)<=k):
        return len(prices)
    n=len(prices)
    prices.sort()
    c=0
    i=0
    flag=0
    cost=k
    while(i<n):
        if(cost>=prices[i]):
            c=c+1
            cost=cost-prices[i]
            i=i+1
        else:
            flag=1
            break
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

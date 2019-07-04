#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    d=dict()
    n=len(orders)
    for i in range(n):
        try:
            d[orders[i][0]+orders[i][1]]=d[orders[i][0]+orders[i][1]]+[i]
        except:
            d[orders[i][0]+orders[i][1]]=[i]
    a=list(d.keys())
    a.sort()
    b=[0]*n
    k=0
    for i in a:
        for j in d[i]:
            b[k]=j+1
            k=k+1
    return b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

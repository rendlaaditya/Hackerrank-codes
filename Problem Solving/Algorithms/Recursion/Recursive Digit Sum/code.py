#!/bin/python3

import math
import os
import random
import re
import sys

def supp(b):
    if len(b)==1:
        return int(b)
    c=0
    for i in b:
        c=c+int(i)
    return supp(str(c))
# Complete the superDigit function below.
def superDigit(n, k):
    a=supp(str(n))
    b=supp(str(k))
    c=supp(str(a*b))
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

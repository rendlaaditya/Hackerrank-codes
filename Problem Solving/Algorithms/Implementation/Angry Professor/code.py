#!/bin/python

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    m=0
    for i in a:
        if(i<=0):
            m=m+1
    if(m>=k):
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = map(int, raw_input().rstrip().split())

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()

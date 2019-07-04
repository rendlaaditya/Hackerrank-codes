#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    a=sum(h1)
    b=sum(h2)
    c=sum(h3)
    i=0
    j=0
    k=0
    while(a!=b or b!=c):
        if(a>b and a>=c) or (a>=b and a>c):
            a=a-h1[i]
            i=i+1
        elif(b>a and b>=c) or (b>=a and b>c):
            b=b-h2[j]
            j=j+1
        elif(c>a and c>=b) or (c>=a and c>b):
            c=c-h3[k]
            k=k+1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = raw_input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = map(int, raw_input().rstrip().split())

    h2 = map(int, raw_input().rstrip().split())

    h3 = map(int, raw_input().rstrip().split())

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

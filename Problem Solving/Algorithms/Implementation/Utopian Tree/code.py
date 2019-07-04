#!/bin/python

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    a=1
    for i in range(n/2):
        a=a*2
        a=a+1
    if(n%2!=0):
        a=a*2
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

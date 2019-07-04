#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    s=max(height)
    if(s<=k):
        return 0
    else:
        return s-k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = map(int, raw_input().rstrip().split())

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()

# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
def insertionSort(arr):
    def inversioncount(p):
        if len(p)==1:
            return [p,0]
        else:
            ai=0
            bi=0
            long(ai)
            long(bi)
            [a,ai]=inversioncount(p[:len(p)/2])
            [b,bi]=inversioncount(p[len(p)/2:])
            c=[]
            i=0
            j=0
            k=0+ai+bi
            long(k)
            while(i<len(a) and j<len(b)):
                if(a[i]<=b[j]):
                    c.append(a[i])
                    i+=1
                else:
                    c.append(b[j])
                    j+=1
                    k=k+len(a)-i
            c+=a[i:]+b[j:]
            return [c,k]
    t=0
    long(t)
    [a,t]=inversioncount(arr)
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

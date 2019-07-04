#!/bin/python

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    d={}
    for i in range(26):
        d[chr(i+97)]=h[i]
    c=-1
    for i in word:
        c=max(c,d[i])
    return len(word)*c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = map(int, raw_input().rstrip().split())

    word = raw_input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    if(n<3):
        return -1
    if(n==3):
        return "555"
    if(n==5):
        return "33333"
    m=n/3
    for i in range(m):
        
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

#!/bin/python3
def fibonacciModified(t1, t2, n):
    for i in range(n-2):
        t3=t1+(t2**2)
        t1=t2
        t2=t3
    print(t3)
t1T2n = input().split()
t1 = int(t1T2n[0])
t2 = int(t1T2n[1])
n = int(t1T2n[2])
fibonacciModified(t1, t2, n)
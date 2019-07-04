#!/bin/python3

# Complete the powerSum function below.
def recur(X,N,i):
    if i**N>X:
        return 0
    if i**N==X:
        return 1
    a=recur(X-i**N,N,i+1)
    b=recur(X,N,i+1)
    return a+b
def powerSum(X, N):
    t=int(X**(1.0/N))+1
    total=recur(X,N,1)
    return total

X = int(input())

N = int(input())

result = powerSum(X, N)

print(str(result))

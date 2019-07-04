#!/bin/python3
# The trick is as follows, if n is a multiple of 2k then, we interchange [1,k] with [k,2k] and so on for rest
# of the 'k' chunks. Else return -1
def absolutePermutation(n, k):
    if k==0:
        return list(range(1,n+1))
    if n%(2*k)==0:
        arr=[]
        temp=k
        for i in range(1,n+1):
            arr.append(i+temp)
            if i%k==0:
                temp=temp*-1
        return arr
    return [-1]
t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    print(*absolutePermutation(n, k))
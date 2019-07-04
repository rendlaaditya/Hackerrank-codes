#!/bin/python3
def gamingArray(arr):
    n=len(arr)
    if n==1:
        return 'BOB'
    m=-1
    cnt=0
    for i in range(n):
        c=arr[i]
        if m<=c:
            m=c
            cnt=(cnt+1)%2
    if cnt:
        return 'BOB'
    return 'ANDY'
g = int(input().strip())
for g_itr in range(g):
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
print(gamingArray(arr))
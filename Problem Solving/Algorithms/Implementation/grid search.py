#!/bin/python3
def search(G,P,u,v):
    a,b=len(P),len(P[0])
    for i in range(u,u+a):
        for j in range(v,v+b):
            if G[i][j]!=P[i-u][j-v]:
                return 0
    return 1
def gridSearch(G, P):
    a,b,c,d=len(P),len(P[0]),len(G),len(G[0])
    irange=c-a+1
    jrange=d-b+1
    for i in range(irange):
        for j in range(jrange):
            if G[i][j]==P[0][0]:
                c=search(G,P,i,j)
                if c==1:
                    return 'YES'
    return 'NO'
t = int(input())
for t_itr in range(t):
    RC = input().split()
    R = int(RC[0])
    C = int(RC[1])
    G = []
    for _ in range(R):
        G_item = input()
        G.append(G_item)
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])
    P = []
    for _ in range(r):
        P_item = input()
        P.append(P_item)
    print(gridSearch(G, P))
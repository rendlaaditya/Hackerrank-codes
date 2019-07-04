t=int(input())
s1=[]
s2=[]
def pushh(a):
    global s1
    global s2
    s1.append(a)
def popp():
    global s1
    global s2
    if s1==[] and s2==[]:
        return -1
    if s2==[]:
        s2=s1[::-1]
        s1=[]
    s2.pop()
def pfront():
    global s1
    global s2
    if s2==[]:
        return s1[0]
    return s2[-1]
for e in range(t):
    r=list(map(int,input().split()))
    if(len(r)>1):
        pushh(r[1])
    else:
        if r[0]==2:
            popp()
        else:
            print(pfront())
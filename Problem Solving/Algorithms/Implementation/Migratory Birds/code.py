n=input()
s=raw_input().split()
t=[]
for i in s:
    t+=[int(i)]
d=dict()
for i in t:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
c=1
for i in d:
    if d[i]>d[c]:
        c=i
    elif d[i]==d[c]:
        if i<c:
            c=i
print c

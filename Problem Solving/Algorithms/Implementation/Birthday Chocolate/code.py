n=input()
s=raw_input().split()
t=[]
for i in s:
    t+=[int(i)]
b=raw_input().split()
d=int(b[0])
m=int(b[1])
u=0
for i in range(n-m+1):
    k=0
    for j in range(m):
        k+=t[i+j]
    if k==d:
        u+=1
print u

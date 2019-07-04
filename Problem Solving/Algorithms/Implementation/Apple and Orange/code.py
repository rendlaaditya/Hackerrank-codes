p=raw_input().split()
s=int(p[0])
t=int(p[1])
q=raw_input().split()
a=int(q[0])
b=int(q[1])
r=raw_input().split()
m=int(r[0])
n=int(r[1])
c=0
d=0
e=raw_input().split()
f=raw_input().split()
for i in e:
    if a+int(i)>=s and a+int(i)<=t:
        c=c+1
for j in f:
    if b+int(j)<=t and b+int(j)>=s:
        d=d+1
print c
print d
    


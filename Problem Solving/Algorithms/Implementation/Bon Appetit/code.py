e=raw_input().split()
n=int(e[0])
k=int(e[1])
s=raw_input().split()
b=input()
t=[]
for i in s:
    t+=[int(i)]
c=t[k]
t.pop(k)
u=0
for i in t:
    u+=i
if u/2==b:
    print 'Bon Appetit'
else:
    print int(float(c)/2)

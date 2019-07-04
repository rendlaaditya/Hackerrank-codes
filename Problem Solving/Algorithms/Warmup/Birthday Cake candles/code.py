n=input()
s=raw_input()
d=s.split()
for i in range(len(d)):
    d[i]=int(d[i])
d.sort()
e=d[-1]
c=0
for i in d:
    if i==e:
        c+=1
print c

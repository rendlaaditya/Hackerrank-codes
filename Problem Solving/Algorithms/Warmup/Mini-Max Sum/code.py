s=raw_input()
d=s.split()
for i in range(len(d)):
    d[i]=int(d[i])
d.sort()
a=d[0]+d[1]+d[2]+d[3]
b=d[1]+d[2]+d[3]+d[4]
print a,b


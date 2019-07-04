s=raw_input().split()
t=int(s[0])
n=int(s[1])
m=int(s[2])
a=raw_input().split()
c=[]
for i in a:
    c+=[int(i)]
b=raw_input().split()
d=[]
for i in b:
    d+=[int(i)]
e=-1
if t>=min(c)+min(d):
    for i in c:
        for j in d:
            if (i+j<=t):
                if i+j>e:
                    e=i+j
    print e
else:
    print e

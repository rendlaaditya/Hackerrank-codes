s=raw_input().split()
n=s[0]
m=s[1]
a=raw_input().split()
t=[]
for i in a:
    t=t+[int(i)]
b=raw_input().split()
u=[]
for j in b:
    u+=[int(j)]
c=max(t)
d=min(u)
if c>d:
    print 0
else:
    w=0
    for k in range(c,d+1):
        q=True
        for i in t:
            for j in u:
                if j%k!=0 or k%i!=0: 
                    q=False
                    break
            if q==False:
                break
        if q==True:
            w+=1
print w

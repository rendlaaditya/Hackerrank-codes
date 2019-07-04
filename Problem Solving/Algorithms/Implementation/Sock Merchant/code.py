n=input()
s=raw_input().split()
t=[]
for i in s:
    t+=[int(i)]
d={}
for i in t:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
c=0
for i in d:
    c=c+(d[i]/2)
print c    

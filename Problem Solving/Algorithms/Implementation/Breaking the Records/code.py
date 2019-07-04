n=input()
s=raw_input().split()
t=[]
for i in s:
    t=t+[int(i)]
a=t[0]
b=t[0]
c=0
d=0
for i in t:
    if i>a:
        c+=1
        a=i
    elif i<b:
        d+=1
        b=i
print c,d
        

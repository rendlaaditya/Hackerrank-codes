n=input()
s=raw_input()
d=0
e=0
for i in s:
    if i=='U':
        d+=1
    else:
        d-=1
    if d==0 and c<0:
        e+=1
    c=d
print e

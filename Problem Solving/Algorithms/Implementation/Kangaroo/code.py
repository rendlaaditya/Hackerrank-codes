s=raw_input().split()
x1=int(s[0])
d1=int(s[1])
x2=int(s[2])
d2=int(s[3])
if d1!=d2:
    if (x1-x2)/(d2-d1)>=0 and (x1-x2)%(d2-d1)==0:
        print 'YES'
    else:
        print 'NO'
elif d1==d2:
    print 'NO'

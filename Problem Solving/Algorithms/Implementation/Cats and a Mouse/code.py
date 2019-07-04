q=input()
for i in range(q):
    s=raw_input().split()
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    if abs(a-c)<abs(b-c):
        print 'Cat A'
    elif abs(b-c)<abs(a-c):
        print 'Cat B'
    else:
        print 'Mouse C'

p=int(input())
q=int(input())
bool=0
for i in range(p,q+1):
    d=len(str(i))
    j='0'+str(i**2)
    # print(j)
    l,r=int(j[:-d]),int(j[-d:])
    if l+r==i:
        bool=1
        print(i,end=' ')
if bool==0:
    print('INVALID RANGE')
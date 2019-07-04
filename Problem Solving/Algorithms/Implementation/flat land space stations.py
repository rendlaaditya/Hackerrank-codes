[n,m]=list(map(int,input().split()))
def flatland(spacests,n,m):
    maxdist=0
    if m==1:
        maxdist=max(spacests[0],abs(n-1-spacests[0]))
        return maxdist
    i=0
    j=0
    spacests.sort()
    while(i<n):
        c=spacests[j]
        if j==0:
            if i<=c:
                maxdist=max(maxdist,abs(c-i))
            else:
                if i!=spacests[j+1]:
                    cc=min(abs(i-c),abs(i-spacests[j+1]))
                    maxdist=max(maxdist,cc)
            if i+1>spacests[j+1]:
                j+=1
        elif j==m-1:
            maxdist=max(maxdist,i-c)
        else:
            if i!=spacests[j+1]:
                cc=min(abs(i-c),abs(i-spacests[j+1]))
                maxdist=max(maxdist,cc)
            if i+1>spacests[j+1]:
                j+=1
        i=i+1
    return maxdist
s=list(map(int,input().split()))
print(flatland(s,n,m))
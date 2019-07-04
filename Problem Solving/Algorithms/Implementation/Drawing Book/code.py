n=input()
p=input()
if n%2==0:
    if p%2==0:
        a=(n-p)/2
        b=p/2
    else:
        a=(n-(p-1))/2
        b=(p-1)/2
else:
    if p%2==0:
        a=(n-(p+1))/2
        b=p/2
    else:
        a=(n-p)/2
        b=(p-1)/2
print min(a,b)        

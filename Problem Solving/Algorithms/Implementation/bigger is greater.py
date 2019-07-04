t=int(input())
def biggernext(arr):
    n=len(s)
    i=n-1
    while(i>0 and s[i-1]>=s[i]):
        i-=1
    if i<=0:
        print('no answer')
        return None
    # print("i=",i)
    j=n-1
    while(arr[j]<=arr[i-1]):
        j-=1
    # print('j=',j)
    arr[i-1],arr[j]=arr[j],arr[i-1]
    arr[i:]=arr[n-1:i-1:-1]
    print(''.join(arr))
for i in range(t):
    s=list(input())
    biggernext(s)
s=raw_input().split()
n=int(s[0])
k=int(s[1])
b=raw_input().split()
t=[]
for i in b:
    t+=[int(i)]
c=0
for j in range(1,n):
    for i in range(j):
        if (t[i]+t[j])%k==0: 
            c+=1
print c

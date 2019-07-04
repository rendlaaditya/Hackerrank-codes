n=input()
x=raw_input()
s=x.split()
for i in range(len(s)):
    s[i]=int(s[i])
c=0
for k in s:
    c+=k
print c    

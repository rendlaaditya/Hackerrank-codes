n=input()
d=' '
f='#'
e=[]
for i in range(n):
    e+=[d*(n-(i+1))+f*(i+1)]
for j in e:
    print j 

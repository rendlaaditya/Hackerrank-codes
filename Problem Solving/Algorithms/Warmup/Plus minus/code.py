N=input()
a=raw_input()
b=a.split()
x=0
y=0
z=0
for i in b:
    if int(i)>0:
        x+=1
    elif int(i)==0:
        y+=1
    else:
        z+=1
print (float(x)/N)
print (float(z)/N)
print (float(y)/N)

A=raw_input()
B=raw_input()
w=A.split()
q=B.split()
Alice=0
Bob=0
for i in [0,1,2]:
    if int(w[i])>int(q[i]):
        Alice+=1
    elif int(w[i])<int(q[i]):
        Bob+=1
print Alice,Bob        


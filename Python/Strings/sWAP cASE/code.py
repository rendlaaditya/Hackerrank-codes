s=raw_input()
y=s.lower()
for i in range(len(s)):
    if i==len(s)-1:
        if s[i]==y[i]:
            y=y[0:i]+y[i].upper()
    else:
        if s[i]==y[i]:
            y=y[0:i]+y[i].upper()+y[i+1:]
print y

s=raw_input()
if s[-2:]=='AM':
    if s[:2]=='12':
        print '00'+s[2:-2]
    else:
        print s[:-2]
elif s[-2:]=='PM':
    if s[:2]=='12':
        print s[:-2]
    else:
        print str(12+int(s[:2]))+s[2:-2]

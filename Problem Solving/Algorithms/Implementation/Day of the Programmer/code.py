n=input()
if n<1918:
    if n%4==0:
        print '12.09.%s'%(str(n))
    else:
        print '13.09.%s'%(str(n))
elif n==1918:
    print '26.09.%s'%(str(n))
else:
    if n%4==0:
        if n%100==0:
            if n%400==0:
                print '12.09.%s'%(str(n))
            else:
                print '13.09.%s'%(str(n))
        else:
            print '12.09.%s'%(str(n))
    else:
        print '13.09.%s'%(str(n))

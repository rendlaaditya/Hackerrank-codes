n=input()
def grader(a):
    if a<38:
        return a
    else:
        if a%5>=3:
            return a+5-a%5
        else:
            return a
for i in range(n):
    b=input()
    print grader(b)



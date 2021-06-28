n=int(input("enter no of elements of the series:"))
x1=0
x2=1
if n==1:
    print(x1)
    exit()
if n==2:
    print(x1)
    print(x2)
    exit()
print(x1)
print(x2)
while (n-2>0):
    next=x1+x2
    print(next)
    x1=x2
    x2=next
    n=n-1
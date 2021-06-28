def factorial(n):
    if n==0 or n==1:
        return 1
    elif n>1:   
        return n*factorial(n-1) 
t=(factorial(10))
print(t)

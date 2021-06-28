def febonacci(n):
   if n==1:
       return 0
   elif n==2:
       return 1
   else:
       return febonacci(n-1)+febonacci(n-2)

print(febonacci(int(input("enter nth element of the series:"))))   
    
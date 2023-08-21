n=int(input())
x=0
while(n>0):
   k=n%10
   x+=k
   n=n//10
   if (n==0 and x<=9):
       print(x)
   elif (n==0 and x>9):
       n=x
       x=0
def is_sdn(n):
    y=n
    x=len(str(y))
    while(n!=0):
        k=n%10
        if(k==0 or y%k!=0):return False
        n=n//10
    return True
    
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(is_sdn(i)==True):
        print(i,end=" ")
def fib(n):
    if n==1:
        return 1
    if n==0:
        return 1
    else:
        p=fib(n-1)+fib(n-2)
        return p
sum=0
m=int(input())
for i in range(m):
    sum=sum+(fib(i)**2)
print(sum)
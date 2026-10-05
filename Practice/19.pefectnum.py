n=int(input("enter num--"))
sum1=0
for i in range(1,n//2+1):
    if n%i==0:
        sum1=sum1+i
if sum1==n:
    print("its perfect",sum1)
else:
    print("its not perfect",sum1)

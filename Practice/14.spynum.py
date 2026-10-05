n=int(input("enter num--"))
sum1=0
mul=1
while n>0:
    digit=n%10
    sum1=sum1+digit
    mul=mul*digit
    n=n//10
if sum1==mul:
    print("spy num")
else:
    print("not spy num")
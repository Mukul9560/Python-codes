n=int(input("enter nm--"))
num=0
digit=0
power=len(str(n))
while n>0:
   digit=n%10
   num=num+digit**power
   n=n//10
print(num)


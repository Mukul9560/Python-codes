n=int(input("enter num--"))
power=len(str(n))
num=0
while n>0:
    digit=n%10
    num=num+digit**power
    power-=1
    n//=10
if num==n:
  print("its disarium",num)
else:
   print("its not disarium",num)
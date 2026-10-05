n=int(input("enter num--"))
digit=0
num=0
while n>0:
   digit=n%10
   num=num*10+digit
   n=n//10
print(num)
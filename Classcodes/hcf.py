# import math
n1=int(input("enter num1--"))
n2=int(input("enter num2--"))
if n1>n2:
    small=n2
else:
    small=n1
HCF=0
for i in range(2,small+1):
    if n1%1==0 and n2%i==0:
        HCF=i
print(HCF)
# print(math.gcd(n1,n2))

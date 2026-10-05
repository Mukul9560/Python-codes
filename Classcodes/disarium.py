n=int(input("enter the num"))
org=n
temp=n 

power=0
while n>0:
    power+=1
    n//=10

add=0
while temp>0:
    last_digit=temp%10
    add=add+last_digit**power
    temp//=10
    power-=1
if add==org:
    print("its disarium num")
else:
    ("its not")

n=int(input("enter the num "))
temp=n
org=n

power=0
while n>0:
    power+=1
    n//=10

add=0
while temp>0:
    last_digit=temp%10
    add = add + last_digit**power
    temp//=10
if add==org:
    print("its armstrong")
else:
    print("its not armstrong")

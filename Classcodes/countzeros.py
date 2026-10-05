n=int(input("enter th num "))
count=0
while n>0:
    last_digit=n%10
    if last_digit ==0:
        count+=1
    n=n//10
print("no of zeros",count)
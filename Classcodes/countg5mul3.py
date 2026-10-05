n=int(input("enter th num "))
countg=0
countmulp=0
while n>0:
    last_digit=n%10
    if last_digit>5:
        countg+=1
    if last_digit%3==0:
        countmulp+=1
    n//=10
print("no. greater than 5 = ",countg)
print("multiple of 3 = ",countmulp)
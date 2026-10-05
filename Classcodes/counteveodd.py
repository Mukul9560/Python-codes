n=int(input("enter th num "))
counteve=0
countodd=0
while n>0:
    last_digit=n%10
    if last_digit%2==0:
        counteve+=1
    else:
        countodd+=1
    n//=10
print("no of even no. ",counteve)
print("no of odd no. ",countodd)
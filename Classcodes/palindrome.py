n=int(input("enter num = "))
org=n
rev=0
while n > 0:
    last_digit=n%10
    rev=rev*10+last_digit
    n=n//10
if org==rev:
    print("palindrome")
else:
    print("not palindrome")

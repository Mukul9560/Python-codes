n= int(input("enter num"))
num=str(abs(n))
if len(num)==1:
    print("one digit")
elif len(num)==2:
    print("two digit")
elif len(num)==3:
    print("three digit")
else:
    print("more than three")

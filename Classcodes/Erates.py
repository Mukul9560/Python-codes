n=float(input("enter units"))
rate=0
if n<=100:
    rate=n*5
    print("rate")
elif n<=300:
    rate=500 + (n-100)*7.5
    print("rate")
elif n<=500:
    rate=500 + 1500 + (n-300)*10
    print("rate")
else:
    rate=500+ 1500+ 2000 + (n-500)*15
    print(rate)
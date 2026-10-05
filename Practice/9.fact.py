n=int(input("enter num--"))
fact=1
if n<0:
    print("factorial not defined")
else:
    while n>0:
     fact=fact*n
     n=n-1
    print(fact)
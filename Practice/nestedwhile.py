n=int(input("enter num"))
i=1
while i<=n:
    print("Multiplication table for",i)
    j=1
    while j<=10:
        print(i,"x",j,"=",i*j)
        j+=1
    i+=1
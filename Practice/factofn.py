n=int(input("enter n"))
i=1
while i<=n:
   fact=1
   j=i
   while j>0:
        fact=fact*j
        j=j-1
   print("factroial of ",i,"=",fact)
   i+=1
n=int(input("enter num"))
fact=[]
for i in range(1,n//2+1):
    if n%i==0:
        fact.append(i)
        i+=1
print(fact)
n=int(input("enter num"))
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
print(count)
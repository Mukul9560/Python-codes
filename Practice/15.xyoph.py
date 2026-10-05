n=int(input("enter num--"))
f=n
l=n%10
m=0
while f>=10:
    f=f//10
    if f>=10:
        m=m+f%10
if f+l==m:
    print("xylem")
else:
    print("phloem")
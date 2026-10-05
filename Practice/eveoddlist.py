l1=[1,2,3,4,5,6,7,8,9]
i=0
l2=[]
l3=[]
while i<len(l1):
    if l1[i]%2==0:
        l2.append(l1[i])
    else:
       l3.append(l1[i])
    i+=1
print(l2)
print(l3)

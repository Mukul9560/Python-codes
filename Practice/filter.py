# filter all the integer values from a list

l1=[10,'hii',2.3,False,30,40,50]
i=0
l2=[]
while i<len(l1):
    if type(l1[i])==int:
        l2.append(l1[i])
    i+=1
print(l2)

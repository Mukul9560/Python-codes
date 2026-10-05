
L1=[["hii", 2 ,"dksf",5]]
num=[]
for i in L1:
    for j in i:
     if type(j)==int :
        fact=1
        for l in range(1,j+1):
            fact=fact*l 
        num.append(fact)
print(num)
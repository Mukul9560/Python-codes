n=int (input("enter amount : "))
m=eval(input("membership True or False :"))
discount=0

if n>10000:
    discount=20
    #if m==True:
     #   discount +=5
elif n>5000:
    discount=10
    #if m==True:
     #   discount +=5   
if m==True:
    discount +=5

bill=n-(n*(discount/100))
print("total",n)
print("discount",discount)
print("membership",m)
print("bill",bill)

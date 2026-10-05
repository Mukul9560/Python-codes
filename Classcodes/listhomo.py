# n=int(input("enter how many values"))
# list_1=[]

# for i in range(n):
#     value=eval(input("enter the value"))
#     list_1.append(value)

l1=eval(input("enter list"))
for i in l1:
    if type(l1[0])!=type(i):
         print("Heterogenous")
         break
else:
  print("homogenous")

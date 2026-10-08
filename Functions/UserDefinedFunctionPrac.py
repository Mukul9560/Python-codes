def sum_of_digit(n):
    add=0
    while n>0:
        add+=n%10
        n//=10
    return add
#print(sum_of_digit(234))

def is_prime(n):
  if n<=1:
   return "not prime"
  else:
    for i in range(2,n):
        if n%i==0:
            return"not prime"
    else:
        return "prime"

# n=int(input("num--"))
# for num in range(1,n+1):
#     if is_prime(num)=="prime":
#        print(num)

n=int(input("enter num"))
for num in range(1,n+1):
   if is_prime(num)=="prime" and is_prime(sum_of_digit(num))=="prime" : 
      print(num)
      
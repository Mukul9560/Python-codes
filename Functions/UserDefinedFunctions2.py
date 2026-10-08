# 3).func without parameter with return val
# 4).func with parameter and with return val

# 3).func without parameter with return val
def my_func():
    for i in range(1,6):
        print(i)
        if i==3:
            return "stop"
# print(my_func())

# create function to get the cube of the value
# create func to get the reverse of num
# create func with return true if the value is even and return false if the value is odd

def cube_func():
     n=int(input('enter num--'))
     return(n**3)

def rev_func():
    n=int(input("num--"))
    return(int(str(n)[::-1]))
#print(rev_func())

def eveodd_func():
    n=int(input("num--"))
    if n%2==0:
        return True
    else:
        return False
#print(eveodd_func())

# 4).func with parameter and with return val

#find the sqr of two num

def sqr_2(num):
   return num**2


def sum_2(a,b):
    return a+b

# create a func is palindrome(n) which return True if n is a palindrome or else returns false

def is_palindrome(n):
    if int(str(n)) == int(str(n)[::-1]):
        return True
    else :
        return False
# print(is_palindrome(34))



def check_palindrome(n):
    if int(str(n)) == int(str(n)[::-1]):
        print("palindrome")
    else :
        print("palindrome")
#check_palindrome(34)

List_1=[11,22,23,101,45,67]
for i in List_1:
    if check_palindrome(i)=="palindrome":

# is_even(n)
# Rev_num(num)
# sum_of_digits(num)
# product_of_digits
# is_odd(num)
# is_perfect(num)
# is_strong(num)
# is_prime(num)
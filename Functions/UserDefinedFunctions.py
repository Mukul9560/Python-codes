
# 1).function with out parameter and without return Val
# 2).function with parameter and  and without return val
# 3).func without parameter with return val
# 4).func with parameter and with return val
# recommended :- function name should be in lowercase

# 1). Function with out parameter and without return Val
# def demo():
#     print("this is demo function")
# def main():
#     print("this is main function")
# demo()
# demo()

# create a function to print n natural numbers
def natural_num():
  n=int(input("enter num"))
  for i in range(1,n+1):
     print(i)


# creating a function to print n natural palindrome number
def palindrome_num():
   n=int(input('enterbnum--'))
   for i in range(1,n+1):
      if str(i)==str(i)[::-1]:
         print(i)



def even_natural():
   n=int(input("enter num--"))
   i=2
   while i<=n:
      print(i)
      i+=2



# even_natural()
# palindrome_num()
# natural_num()
# demo()
# main()

# 2). Functions with parameters and without return val
#  def func_name(var1,var2,----,var n):
#     logic:
#
#   func_name(var1,var2,----,var n)
# the number of parameters must be equal to no. of arguments

def demo(a,b,c):
   print('hi')
   print(b)
   print(c)


def sqr_1(num):
   num=int(input("enter num"))
   print(num**2)


def sqr_2(num):
   print(num**2)


list=[10,34,5]
for i in list:
   print(sqr_2(i))

# Decorators
# - It is used to extra functionality to a function without modifying the main function
# - It is used before a function with the symbol '@'
# - There are two types of decorators
# 1). Inbuilt Decorator 
# --> classmethod,staticmethod,abstractmethod,property
# 2). User Defined Decorator
# --> These are the decorators defined by the user according to its requirement
# --> Decorator is a function which takes another function as input and also returns a function i.e.,wrapper function
# --> It is defines with the help of a nested function

# How to define a decorator
# Syntax:-
# def decorator_name():
#              def wrapper(**args,**kwargs):
#                   PRE TASK
#                   func(*args,**kwargs)
#                   PAST TASK
#              return wrapper

# How to use use the decorator
# Syntax:
#       @decorator_name()
#       def func_name():
#           STATEMENT BOX
#       func_name()

# How decorator is called internally
#  func_name=decorator_name(func_name)
                     

def instagram(func):
    def wrapper(*args,**kwargs):
        print("www.insta.com")
        print("Logged in")
        func(*args,**kwargs)
        print("Log out")
    return wrapper
@instagram
def sourav_insta():
    print('posted story')
@instagram
def tushar_insta():
    print("msg girls")
@instagram
def mukul_insta():
    print("watches reels")

sourav_insta()
mukul_insta()
tushar_insta()
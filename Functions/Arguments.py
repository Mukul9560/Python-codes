# Parameters (formal arguments)
# these are the variables defined during the definition of functions
# used to receive the arguments/values passed to functions
# also known as formal arguments 

# Arguments (actual arguments)
# these are the values passed to the functions during thr functions call

#types of arguments
# 1). positional arguments
# 2). keyword arguments
# 3). default arguments
# 4). variable length arguments
# 5). variable length keyword arguments

# 1).Positional arguments
# These are passed with respect to the position
# here order and position matters
# in this no. of parameters should be equal with the no. of arguments
def demo(a,b,c):
    print(a)
    print(b)
    print(c)
demo(10,20,30)
#
# 2). Keyword Argument:-
# In this argument are passed with the help of keys
# here parameters are the keys
# in this order and position doesn't matter however the number of parameters must be equal to the no. of values
# positional arguments should be defined before the keyword arguments
def person(name,age):
    print('name',name)
    print('age:',age)
person(age=24,name='rohit')

#3). Default Argument:-
# the default value which are defined during the function definition
# if user doesn't pass the value then default value is considered
# here the no arguments can be equal or less than the no. of parameters
# here order and position matters
def person(name,age,email='N/A'):
    print('name',name)
    print('age:',age)
    print('email',email)
person(age=24,name='rohit',email='g@mail.com')


# 4). variable length arguments
# it is used to receive n no. of positional arguments
# it is denoted by args
# it stores multiple values in tuple

def students_attendance(*args):
    print(args,type(args))

# students_attendance()
# students_attendance('neel')
# students_attendance('nitin','neel')

def add(*args):
    add=0
    for i in args:
        add=add+i
    return add
# print(add(9,3))
# print(add(8,5,6))

# 5). variable length keyword argument
# it is used to receive n no. of keyword argument
# it is denoted by **kwargs
# it stores all the keywords arguments in a dictionary

def products(**kwargs):
    print(kwargs,type(kwargs))
# products()
# products(camera=2,laptop=3,phone=4)


# using both *args and **kwargs both

def demo(*args,**kwargs):
    print(args)
    print(kwargs)
demo(10,20,30,a=99,b=45,c=32)
#demo(a=99,b=45,c=32)
# Scope of variable
# It states the distance till where we can access the variable
# there are four scopes for a variable
#1).Local scope
#2).Enclosed/Non-local scope
#3).Global scope
#4).Built in scope
# In python it follows LEGB rule for the scope of variable python
# 
# [Built in[Global[Non local[local]]]]


# Global Scope :- 
# If we declare a variable in main space then it is considered as 'global scope'.
# We can access it inside the main space , enclosed space as well as in local space also.

# Local Scope :-
# If we declare a variable inside a function then its considered as local scope
# We ca access this variable inside the 
# 
def demo():
    b=20  #Local variable
    print(b)
demo()

a=10     # Global Variable
def demo():
    b=20
    print(b)
demo()

# global - it helps us to modify the global variable in a local scope

# Non-Local/Enclosed Scope :-
# when we have nested functions, then the variable present inside the inner most function is known as local
# ,variable present in the main space is known as global variable and all the variables present inside the 
# outer functions are known as non-local variable /enclosed variable 

a=10           # Global variable 
def outer():
    b=20       # enclosed variable
    def inner():
        c=38   # local variable
        print(c)
    inner()
outer()

# Non-local keyword - it helps us to modify the non local variable inside the local space
# Built in space - 
# it is a pre-defined scope which can be accessed in any python module
# all the pre-defined functions ,variables, keywords have the built in scope

# Ex:- print(),input(),True,None,False,rtc.
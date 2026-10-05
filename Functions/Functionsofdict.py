# Functions of dictionary
# Fetching keys,values from dict : var[key]
# 1). get() :- var.get(Key,default_val)
# 2). keys()
# 3). values()
# 4). items()
# Adding items in dict : var[key]=val
# 1). update()
# 2). setdefault() :-
#  if we pass only key then it keep the value as none by default
#  cannot update the val of the existing key
# 3). fromkeys() :- var.fromkeys(iterable,val)
#  converts iterable into a dictionary where all the values of iterable become keys
#  by default the value is none
#  Remaining items from dict
# 1). pop(key)
# 2). popitem()
# 3). clear()
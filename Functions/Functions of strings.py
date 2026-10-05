
# Functions of Strings --> 
# 1). upper() : Syntax : var.upper()
# 2). lower() : Syntax : var.lower()
# 3). swapcase() : Syntax : var.swapcase()--change lower chr to upper and vice versa
# 4). capitalize() : Syntax : var.capitalize()--convert the first chr of string to capital & convert rests to lowercase
# 5). title() : Syntax : var.title()--convert all the words first letter to capital
# 6). isupper() : Syntax : var.isupper()
# 7). islower():- :- Syntax : var.islower()
# 8). istitle() :- Syntax : var.istitle()
# 9). isdigit() :- Syntax : var.isdigit()
# 10). isalpha() :- Syntax : var.isalpha()
# 11). isalnum() :- Syntax : var.isalnum()
# 12). isspace() :- Syntax : var.isspace()
# 13). isstartswith() :- Syntax : var.isstartswith()
# 14). isendswith() :- Syntax : var.isendswith()
# 15). replace() :- Syntax : var.replace(old_str,new_str,r)
# 16). count() :- Syntax : var.count() -- counts no. of repetition
# 17). index() :- Syntax : var.index('chr')
# 18). rindex() :- Syntax : var.rindex()
# 19). find() :- Syntax : var.find()
# 20). rfind() :- Syntax : var.rfind('chr')
# 21). strip() :- Syntax : var.strip('chr')
# 22). lstrip() :- Syntax : var.lstrip('chr')
# 23). rstrip() :- Syntax : var.rstrip('chr')
# 24). split() :- Syntax : var.split()
# -- splits the string into multiple sub strings
# -- returns a list of strings
# -- default val is space 
# 25). join() :- Syntax : var = 'chr'.join(iterable) 
# -- iterable should contains only string data 
# -- used to join multiple substrings by the help of given character
# -- returns a string


# s='HELlo124'
# s=s.swapcase()
# print(s)
# s='tHIs IS my StrinG'
# s=s.capitalize()
# print(s)
# s='t'
# print(s.islower())

# WAP to check given chr is special chr or not
# WAP to extract all uppercase,lowercase,numbers and special char in different lists
# Extract all palindrome words from list and keep it in uppercase in other list
# l1=['hello','level','madam','python']
# out=['LEVEL','MADAM']

# #1).
# s=str(input("enter the string"))
# if s.isalnum():
#     print("not special")
# else:
#     print("special")



# #2).
# s=str(input("enter string--"))
# U1=[]
# L1=[]
# N1=[]
# S1=[]
# for i in s:
#     if i.isupper():
#         U1.append(i)
#     elif i.islower()  :
#         L1.append(i)
#     elif i.isdigit  :
#         N1.append(i)
#     elif:
#         S1.append(i)
# print(U1)
# print(L1)
# print(N1)
# print(S1)


#3).
# out=[]
# for i in l1:
#     if i == i[::-1]:
#         out.append(i.upper())
# print(out)

s='on your left'
a=s.split()
print(' '.join(a[::-1]))

b=100
p=input("peak hours True or False")=="True"
r=input("rainy weather True or False")=="True"
h=input("holiday True or False")=="True"
f=b
'''if p:
    f=f+(50/100)*100
if r:
    f=f+(20/100)*100
if h:
    f=f+(30/100)*100'''
extra=0
if p:
    extra +=50
if r:
    extra +=20
if h:
    extra +=30
print("final fare",f+(f*extra/100))
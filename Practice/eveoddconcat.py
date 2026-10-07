In=int('127342')
str1=''
str2=''
while In>0:
    i=In%10
    if i%2==0:
        str1.append(str(i))
    else :
        str2.append(str(i))
    In=In//10
print(str1+str2)
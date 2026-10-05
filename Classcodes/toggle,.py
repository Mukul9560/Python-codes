s='HEllo233'
i=0
# new=''
# while i<len(s):
#     if 'A'<=s[i]<='Z' :
#         new +=s[i].lower()
#     else:
#         new +=s[i].upper()
#     i+=1
# print(new)
out=''
for i in s:
    if 'A'<=i<='Z':
        out+=chr(ord(i)+32)
    elif 'a' <=i <= 'z':
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)
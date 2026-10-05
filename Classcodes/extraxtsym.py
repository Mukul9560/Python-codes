s='Adimn@#$%12'
symbols=''
i=0
while i<len(s):
    if not ('A'<=s[i]<='Z' or 'a'<=s[i]<='z' or '0'<=s[i]<='9'):
        symbols+=s[i]
    i+=1
print(symbols)
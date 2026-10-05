S="hai hello"
out={}

for i in S.split():
    v=""
    for j in i:
        if j in "aeiou":
            v=v+j
    out[i]=v
print(out)
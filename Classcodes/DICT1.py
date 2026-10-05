s="push maadi kushi padi"
out={}
for i in s.split():
    if len(i)%2==0:
        out[i]=i[0]+i[-1]
    else:
        out[i]=i[len(i)//2]
print(out)
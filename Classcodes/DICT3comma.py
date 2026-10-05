S=['jiocinema.com','file.py','wen.html','amazon.com','www.org']
out=[]

# for i in S:
#     v=""
#     for j in i:
#        if j== ".":
#            v=""
#        else:
#            v=v+j
#     out.append(v)
# print(out)

for i in S:
    ex=i.split('.')[-1]
    if ex not in out:
        out.append(ex)
print(out)
S=['jiocinema.com','file.py','wen.html','amazon.com','www.org','python.py']
out={}

for i in S:
    a,b=i.split('.')
#     out.setdefault(b,[]).append(a)
# print(out)

    if b not in out:
      out[b]=[a]
    else:
      out[b]+=[a]
print(out)
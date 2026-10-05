list1=['Hello','java','India']
out=set()
for i in list1 :
   for j in i:
        if j in 'AEIOUaeiou':
            out.add(j)
print(out)
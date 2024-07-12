a="amit is a good boy"
b=[]
for i in a.split():
    b.append(i)
print(b)
c=[]
for i in b:
    if(i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u'):
        d=i[0].upper()
        c.append(d+i[1:])
    else:
        c.append(i.lower())
d=" ".join(i for i in c)
print(d)
a="I Love India"
p=a.split()
c=[]
for i in p:
    c.append(i[::-1])
# d=' '.join(map(str,c))
d=' '.join([str(ele) for ele in c])
print(d)
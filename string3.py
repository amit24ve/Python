a="ami@^#*$&%vr9472"
c=""
d=""
e=""
for i in range(len(a)):
    if(a[i].isalpha()):
        c+=a[i]
    elif(a[i].isnumeric()):
        d+=a[i]
    else:
        e+=a[i]
print(len(c))
print(len(d))
print(len(e))
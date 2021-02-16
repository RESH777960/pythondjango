f=open("teams","r")
lst=[]
for name in f:
    lst.append(name.rstrip("\n"))
print(lst)
st1=set(lst)
print(st1)


f1=open("drop","r")
lst2=[]
for name in f1:
    lst2.append(name.rstrip("\n"))
print(lst2)
st2=set(lst2)
print(st2)


diff=st1.difference(st2)
print(diff)

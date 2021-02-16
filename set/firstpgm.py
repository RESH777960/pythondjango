st={}
print(type(st))
st=set()
print(type(st))
dict={20,"hello",38,54}
print(dict)
print(type(dict))
st={10,20,"hello",32}
dict.update(st)
print(dict)
print(st)
for num in st:
    print(num,end=" ")

print()
lst=[10,20,20,"hello"]
st1=set(lst)
print(st1)
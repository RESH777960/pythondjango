lst=[1,2,3,4,5,6]
#pgm for more than one pairs
no=int(input("enter the number"))
st=set(lst)
out=set()
for num in st:
    op=no-num
    if op in st:
        if op>num:
            out.add((num,op))
        else:
            out.add((op,num))

print(out)
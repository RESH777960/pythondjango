lst=[1,2,3,7]
no=int(input("enter the number"))
st=set(lst)
for num in st:#complexity less hash table comparison
    op=no-num
    if op in st:
        print(num,op)
        break
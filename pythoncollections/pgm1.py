lst=[
    [10,20,30],
    [10,20,30],
    [50,60,70]
]
lst2=[]
for num in lst:
    print(num)
    for val in num:
        lst2.append(val)
    print(lst2)

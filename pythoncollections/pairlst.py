lst=[1,2,3,4]
total=sum(lst)
for num in lst:
    diff=total-num
    if(diff==8)|(diff==6):
        print(num)

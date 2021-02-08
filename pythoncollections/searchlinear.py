arr=[10,11,12,13,14]
element=int(input("enter the element for search"))
flg=0
for num in arr:
    if(element==num):
        flg=1
        break
    else:
        pass
if(flg==0):
    print("element not found")
else:
    print('element found')

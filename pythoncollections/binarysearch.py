arr=[11,12,10,23,32]
element=int(input("enter the element for search"))
arr.sort()#method calling
#dat=sorted(arr)#function calling
print("sorted array is")
print(arr)
low=0
flg=0
upper=len(arr)-1
while(low<upper):
    mid=upper+low//2
    if(element<arr[mid]):
        upper=mid-1

    elif(element>arr[mid]):
        low=mid+1
    elif(element==arr[mid]):
        flg=1
        break
    else:
        pass
if(flg==1):
    print("element found")
else:
    print("not found")


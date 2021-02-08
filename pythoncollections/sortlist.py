arr=[11,12,13,10,15]
temp=0
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)-1):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            pass
print(arr)
#########################################################################################################


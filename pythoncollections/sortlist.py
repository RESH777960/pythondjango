arr=[11,12,13,10,15]
#arr=[12,15,11,10,19,16]
temp=0
for i in range(0,len(arr)):
    for j in range(len(arr)):
        if(arr[i]<=arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        else:
            pass
print(arr)
#########################################################################################################


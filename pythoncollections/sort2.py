lst1=[10,20,30,60,90]
lst2=[10,20,40,50,80]
pos1=0
pos2=0
while(pos1<len(lst1)&(pos2<len(lst2))):
    if(lst1[pos1]==lst2[pos2]):
        print(lst1[pos1])
        pos1+=1
        pos2+=1
    elif(lst1[pos1]>lst2[pos2]):
        pos2+=1

    else:
        pos1+=1

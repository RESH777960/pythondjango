num=int(input("enter the number"))
sum=0
while(num!=0):
    digit=num%10
    sum+=digit**3
    #print(end="")
    num//=10
print(sum)



num=int(input("enter the number"))
res=""
while(num!=0):#123!=0 12!=0 1!=0
    digit=num%10# digit=3 digit12%10=2 1%10=1
    #print(digit,end="")#321
    res=res+str(digit) #""+"3"="3"+"2"="32"

    num=num//10
print(res)
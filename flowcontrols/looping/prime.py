limit=int(input("enter the num"))
flg=0
for i in range(2,limit):
    if (limit%i==0):
        flg+=1
        break
    else:
        flg=0
if (flg==0):
        print(" prime")
else:
        print("not prime")




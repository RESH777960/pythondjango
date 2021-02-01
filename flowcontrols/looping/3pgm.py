i=1
osum=0
esum=0
limit=int(input("enter limit"))
ecount=0
ocount=0
while(i<=limit):

    if i%2==0:
      esum+=i
      ecount+=1

    else:
        osum+=i
        ocount+=1

    i+=1




print(osum)
print("odd count is",ocount)
print(esum)
print(ecount,"even count is")

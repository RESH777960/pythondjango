num=int(input("enter number "))
sum=0
for i in range(1,num+1):
    pattern=(str(num)*i)
    print(pattern,end=" ")
    sum=sum+int(pattern)
print("\n")
print("Sum is ",sum)



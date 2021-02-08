num=int(input("enter the number"))
llimit=int(input())
ulimit=int(input())
for i in range(1,(ulimit+1)):
    if (i**num) in range(llimit,(ulimit+1)):
        print((i**num))


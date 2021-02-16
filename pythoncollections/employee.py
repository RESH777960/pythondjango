employees=[
    [10,'tom','developer',1000],
    [20,'peter','debugger',2000],
    [30,'sam','tester',3000]
]
sum=0
for emp in employees:
    print(emp[1])
for emp in employees:
    if(emp[2]=="developer"):
        print(emp)
for emp in employees:
    sum=sum+emp[3]
print(sum)
######################################################################################
sal=0
for emp in employees:
    if(emp[3]>sal):
        sal=emp[3]
print(sal)
##################################memory space complexity high
lst2=[]
for emp in employees:
    lst2.append(emp[3])
print("high salary" ,max(lst2))


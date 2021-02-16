employee=[
    [10,'tom','developer',1000,1997,2000],
    [20,'peter','debugger',2000,1996,2000],
    [30,'sam','tester',3000,1998,2000]
]
# dif=0
# new_lst=[]
# lst=0
#
# for exp in employee:
#          dif=exp[5]-exp[4]
#          new_lst.append(dif)
# m=max(new_lst)
# for exp in employee:
#     dif=exp[5]-exp[4]
#     if dif==m:
#         print(exp)
#######################################################################################################################################second method
val=0
dif=0
for emp in employee:
    if (dif<emp[5]-emp[4]):
        dif=emp[5]-emp[4]
        val=emp
print(dif,val)
#############################################################################################################



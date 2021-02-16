#keys id name desig salry
#print employee name
#employe salary
#chk for gender key is there if not add gender key value pair
#iterate all key value pairs
employee={"id":1000,"name":"ram","designation":"manager","salary":40000}
print(employee["name"])
print(employee["salary"])


if "gender" in employee:
    print("entry exist")
else:
    employee["gender"]="female"
print(employee)

for k in employee:
    print(k)



for k,v in employee.items():
    print(k,":",v)

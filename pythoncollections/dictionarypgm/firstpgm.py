expens={"jan":28000,"feb":40000,"march":45000}
print(expens)


print(expens["feb"])

expens["feb"]-=1000
print(expens)

expens["june"]=450000
print(expens)


if "feb" in expens:
    print("entry exist")
else:
    print("no entry ")
#chk for july entry if not add july=529090

if "july" in expens:
    print("entry exist")
else:
    expens["july"]=529090

print(expens)



for item in expens:
    print(item)


for k,v in expens.items():
    print(k,":",v)
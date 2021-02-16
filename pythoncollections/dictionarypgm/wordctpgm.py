text="ABBC"
dict={}
for chr in text:
    if chr in dict:
        print(chr,"is first recursive character")
        break
    else:
        dict[chr]=1


# print("the first recursive character is:")
# print(dict[])


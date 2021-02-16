text="hello hai hello hai hello"
words=text.split(" ")#stored in list format
#print(words)
dict={}
for word in words:
    if word not in dict:
        dict[word]=1

    else:
        dict[word]+=1
print(dict)
# for word in words:#for adding string in dictionary
#     if word not in dict:
#         dict[word]=1
#     else:
#         dict[word]+=1
#         print("most repti word",word)
#         break

#print(dict)
#######################################################################################methods
print(dict.get("hello"))# function for getting value
#print(max(dict))#if we add yard yard will be the most repti#find max using key
print(max(dict,key=dict.get))
######################################################################################################
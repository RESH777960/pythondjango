#file I/O
#file used to store data
#file operations- read , write and append
#file=open(path,mode of operation)
#read-r
#write-w
#append-a
#rstrip function remove '\n'
# ################################################################################first pgm
f=open("demo","r")
# for lines in f:
#     print(lines)
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
st=set(lst)
print(st)


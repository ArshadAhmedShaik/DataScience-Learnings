# name = "Harry"
# name = list(name)
# start = 0
# end = len(name)-1
# while(start<end):
#       temp = name[start]
#       name[start] = name[end]
#       name[end] = temp
#       start += 1
#       end -= 1
# name = "".join(name)      
# print(name)   

name = "Harry01234567"
# print(name[0:10:n]) #skip n-1 chars
print(name[0:10:1]) #skip 0 chars
print(name[0:10:2]) #skip 1 chars
print(name[0:10:4]) #skip 3 chars
print(name[0:10:5]) #skip 4 chars

print(name[:19]) # replace first number with 0
print(name[1:]) # replace second number with len(name)-1




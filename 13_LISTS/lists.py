name = "Arshad"
name_list = list(name)
print(name_list)
start = 0
end = len(name_list)-1
while(start<end):
     temp = name_list[start]
     name_list[start] = name_list[end]
     name_list[end] = temp
     start += 1
     end -= 1
print(name_list) 
res = ".".join(name_list)
print(res)   
print(type(res))  
marks = [54, 23, 35, 45]
print(marks[0:3])
name_list.extend(["Arshad", True, False])
print(name_list)


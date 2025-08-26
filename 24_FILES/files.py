f = open("arshad.txt", "r") #read in text mode, binary files: "rb"

content = f.read()
print(type(content))
print(content)
f.close()
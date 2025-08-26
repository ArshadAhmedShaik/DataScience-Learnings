import os

# a = os.listdir("dir")
# print(a)
# print(type(a)) 

# get current working directory
print(os.getcwd())

# checks if directory/path exists or not
print(os.path.exists("arshad"))

#cannot remove  directories
os.remove("sample_file.txt")

# to remove empty directories
os.rmdir("dir")
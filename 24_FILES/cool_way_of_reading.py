# f = open("arshad.txt", "r")
# content = f.read()
# print(content)
# f.close()

# context manager
with open("arshad.txt", "r") as f:
  content = f.read()
  print(content)
  # no need to write f.close() beacuse file is 
  # already closed by with
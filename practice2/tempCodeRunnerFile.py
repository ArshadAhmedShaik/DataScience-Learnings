with open("arshad.txt", "r") as f:
      line = f.readline()
      while line:
            print(line.strip())
            line = f.readline()
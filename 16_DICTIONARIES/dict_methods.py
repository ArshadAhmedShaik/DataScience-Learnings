marks = {"Harry": 34, "Jack": 45, "lily":94 }

print(marks.keys())
print(marks.values())
print(marks.items())
for x in marks.items():
    print(x)
print(marks.pop("Harry"))
print(marks)
print(type(marks.keys()))


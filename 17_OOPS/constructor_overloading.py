# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#   def sum(self, p):
#     return Point(self.x + p.x, self.y + p.y)

# p1 = Point(3,2)
# p2 = Point(6,3)
# p3 = p2.sum(p1)
# print(p3.x, p3.y)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def sum(self, p1, p2):
    return Point(p1.x+p2.x, p1.y+p2.y)
  def __add__(self, p):
    return Point(self.x+p.x, self.y+p.y)
  
p1 = Point(1,2)
p2 = Point(3,4)

p3 = p2.sum(p1, p2)
print(f"({p3.x},{p3.y})")

p3 = p1 + p2
print(f"({p3.x},{p3.y})")




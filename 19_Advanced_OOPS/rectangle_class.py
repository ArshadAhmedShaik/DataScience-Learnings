class Rectangle:
      def __init__(self, width, height):
            self.width = width
            self.height = height

      @property
      def area(self):
          return self.width*self.height
      
      @property
      def perimeter(self):
           return 2*(self.width+self.height)
      
      @property
      def square(self):
           return self.width == self.height

      @square.setter
      def square(self, value):
          if value:
               self.height = self.width


r = Rectangle(4,5)
print(r.area)   
print(r.perimeter)  
print(r.square)
r.square = True
print(r.square)   
print(r.width, r.height)  

                   
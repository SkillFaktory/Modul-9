class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width 
        self.height = height

    def _str_(self):
        return 'Rectangle({}, {}, {}, {})'.format(self.x, self.y, self.width, self.height)

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return 'Circle({}, {}, {})'.format(self.x, self.y, self.r)

rect = Rectangle(5, 10, 50, 100)
print(rect)

circle = Circle(2, 7, 10)
print(circle)
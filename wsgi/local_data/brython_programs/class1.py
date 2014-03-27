'''
# Circle.py
import math

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def contains(self, point):
        dx = point[0] - self.center[0]
        dy = point[1] - self.center[1]
        return math.sqrt(dx*dx + dy*dy) < self.radius

# Circle.py
import math

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def contains(self, point):
        dx = point[0] - self.center[0]
        dy = point[1] - self.center[1]
        return math.sqrt(dx*dx + dy*dy) < self.radius
    def getradius(self):
        return self.radius
    def getcenter(self):
        return self.center
    def setradius(self, r):
        self.radius = r
    def setcenter(self, c):
        self.center = c

c = Circle([3,4], 5)
print(round(c.area(),3), round(math.pi*math.pow(5,2), 3))
'''
# Geometry.py
import math

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def contains(self, point):
        dx = point[0] - self.center[0]
        dy = point[1] - self.center[1]
        return math.sqrt(dx*dx + dy*dy) < self.radius

class Square:
    def __init__(self, ll, side):
        self.lowerleft = ll
        self.side = side

    def area(self):
        return self.side * self.side
    def contains(self, point):
        dx = point[0] - self.lowerleft[0]
        dy = point[1] - self.lowerleft[1]
        if dx < 0 or dx > side:
            return False
        if dy < 0 or dy > side:
            return False
    
def unitcircle():
    return Circle([0, 0], 1)

def unitsquare():
    return Square([0, 0], 1)

square = unitsquare()
circle = unitcircle()
print(square.area(),"還有",circle.area())

class Square:
   def __init__(self, x):
      self.a = x

   def area(self):
      print(self.a * self.a)


sq = Square(12)
sq.area()

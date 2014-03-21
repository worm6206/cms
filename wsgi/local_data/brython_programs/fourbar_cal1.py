from math import *

# 點類別定義
class Point:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)
    def __str__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)
    def distance(self, pt):
        self.pt = pt
        return sqrt(pow(self.x - self.pt.x,2) + pow(self.y - self.pt.y,2))
    def Eq(self, pt):
        self.x = pt.x
        self.y = pt.y
    def setPoint(self, px, py):
        self.x = px
        self.y = py

# 線類別定義
class Line:
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
        self.Tail, self.Head = self.p1, self.p2
    def length(self):
        return sqrt((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)
    def setPP(self, p1, p2):
        self.p1, self.p2 = p1, p2
        self.Tail, self.Head = self.p1, self.p2
    def setRT(self, r, t):
        self.r = r
        self.t = t
        x = self.r * cos(self.t)
        y = self.r * sin(self.t)
        self.Tail.Eq(self.p1)
        self.Head.setPoint(self.Tail.x + x, self.Tail.y + y)
    def setTail(self, pt):
        self.pt = pt
        self.Tail.Eq(pt)
        self.Head.setPoint(self.pt.x + self.x, self.pt.y + self.y)
    def getR(self):
        x = self.p1.x - self.p2.x
        y = self.p1.y - self.p2.y
        return sqrt(x * x + y * y)
    def getT(self):
        x = self.p2.x - self.p1.x
        y = self.p2.y - self.p1.y
        if (abs(x) < 1E-100):
            if y < 0.0:
                y = -pi/2
            else:
                y = pi/2
        else:
            return atan2(y, x)
    def getHead(self):
        return self.Head
    def getTail(self):
        return self.Tail

# 三角形類別定義
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1, self.p2, self.p3 = p1, p2, p3
    # 求邊長
    def getLenp3(self):
        return self.p1.distance(self.p2)
    def getLenp2(self):
        return self.p1.distance(self.p3)
    def getLenp1(self):
        return self.p2.distance(self.p3)
    # 求角度
    def getAp1(self):
        return acos(((self.getLenp2() * self.getLenp2() + self.getLenp3() * self.getLenp3()) \
        - self.getLenp1() * self.getLenp1()) / (2* self.getLenp2() * self.getLenp3()))
    def getAp2(self):
        return acos(((self.getLenp1() * self.getLenp1() + self.getLenp3() * self.getLenp3()) \
        - self.getLenp2() * self.getLenp2()) / (2* self.getLenp1() * self.getLenp3()))
    def getAp3(self):
        return acos(((self.getLenp2() * self.getLenp2() + self.getLenp1() * self.getLenp1()) \
        - self.getLenp3() * self.getLenp3()) / (2* self.getLenp2() * self.getLenp1()))

deg = pi/180
x1 = 0
y1 = 10
r = 10
# 旋轉 360 度
for 索引 in range(361):
    角度 = 索引*deg
    x2 = x1 + r*cos(角度)
    y2 = y1 - r*sin(角度)
    p1 = Point(x2, y2)
    #p1 = Point(10, 10)
    p2 = Point(x1, y1)
    p3 = Point(0, 20)
    triangle1 = Triangle(p1, p2, p3)

    #print(triangle1.getLenp3())
    print("長度")
    print(round(triangle1.getLenp2(), 4))
    #print(triangle1.getLenp1())
    print("角度")
    print(round(triangle1.getAp3(), 4))
    print()

'''
line1 = Line(p1, p2)
print(p1)
print(line1.length())
'''
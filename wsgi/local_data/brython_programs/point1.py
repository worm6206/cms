import math
import time
from browser import doc
import browser.timer

canvas = doc["plotarea"]
context = canvas.getContext("2d")

class Point():
    # px: 點的 x 座標
    # py: 點的 y 座標
    # pn: 點的名稱
    # A: 來源點物件
    # name, x, y are the attributes of the class
    # name, x, y 為點類別的物件屬性
    # x, y, name are global variables, x, y are float and name is string
    def __init__(self, px=0, py=0, pn="", A=None):
        # A is a Point, pn is a String, px, py is coordinates,
        self.x = px
        self.y = py
        self.name = pn
        self.A = A
        if(A != None):
            self.x = A.x
            self.y = A.y
    def drawMe(self, ctx=None, d=1):
        ctx.beginPath()
        # 利用 fillRect 繪製一個長寬各 1 單位的正方形
        ctx.fillRect(self.x, self.y, 1, 1)
        self.showStrokeText(ctx, self.name, "#000000")
        ctx.stroke()
        #ctx.restore()

    def showStrokeText(self, ctx, text, color):
        ctx.strokeStyle = color
        ctx.font = '10px san-serif'
        ctx.textBaseline = 'bottom'
        ctx.strokeText(text, self.x+10, self.y+10)

class Vector():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
      
    def setXY(self, px=None, py=None):
        self.a = px
        self.b = py
    def setRT(self, pr=None, pt=None):
        self.a = pr*math.cos(pt)
        self.b = pr*math.sin(pt)
    # A, B are Point
    def setPP(self, A=None, B=None):
        self.a = B.x - A.x
        self.b = B.y - A.y
    # p is vector
    def dot(self, p=None):
        return self.a*p.x + self.b*p.y

# 用 px, py 與 pn 來定義點
p2 = Point(px=4, py=5, pn="這是點物件")
print(p2.A)
# 用 A 與 pn 定義點
p3 = Point(pn="直接用點物件定義點", A=p2)
print(p3.A, p3.A.x, p3.A.y)
print(p2.x, p2.y, p2.name, p3.x, p3.y, p3.name)
# 用 px, py 與 pn 來定義點
p1 = Point(px=0, py=5, pn="指定點的 x 與 y 座標")
print(p1.x, p1.y, p1.name)
# 用 A 與 pn 定義點
p4 =Point(A=p3, pn="這是 p4 點")
# 直接用 A 來定義點
p5 = Point(A=p1)
p5.name = "這是 p5 點"
print(p4.name, p4.x, p4.y, p5.x, p5.y, p5.name)
# 也可以依照輸入參數的順序來定義點, 沒有輸入的欄位使用內定值
p6 = Point(1, 2, "點 6")
print(p6.x, p6.y, p6.name)
p7 = Point(9, 8)
print(p7.x, p7.y, p7.name)
count = 0
deg = math.pi/180
for i in range(0, 360, 10):
    count += 1
    print("第", count, "個點")
    point = Point(200+100*math.cos(i*deg), 200-100*math.sin(i*deg), str(count))
    point.drawMe(context)
center = Point(200, 200)
center.drawMe(context)
'''
以上使用 Python 架構 method overloading 好像比 Java 簡單, 但是實際上
仍然犧牲到某些成分, 因為若 px, py 不是整數或浮點數, 若 pn 不是字串
若 A 不是點資料, 上述設計都沒能著墨, 所以程式其實沒有捷徑, 只是採用
不同方法, 各取所需!
'''

# Pythonic way to argument overloading
def sum(*summands):
    result = 0
    for summand in summands:
        result += summand
    return result
print(sum(1, 2, 3, 4))
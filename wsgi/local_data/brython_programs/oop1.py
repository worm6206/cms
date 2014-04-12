class Point():
    # px: 點的 x 座標
    # py: 點的 y 座標
    # pn: 點的名稱
    # A: 點物件
    # name, x, y are the attributes of the class
    # name, x, y 為點類別的物件屬性
    # x, y, name are global variables, x, y are float and name is string
    def __init__(self, px=None, py=None, pn=None, A=None):
        # A is a Point, pn is a String, px, py is coordinates,
        self.px = px
        self.py = py
        self.pn = pn
        self.A = A
        # 只有 pn 與 A
        if (pn != None and A != None and px == None and py == None):
            self.name = pn
            self.x = A.x
            self.y = A.y
        # 只有 px 與 py
        elif (px != None and py != None and pn == None):
            self.name = ""
            self.x = self.px
            self.y = self.py
        # 只有 px, py, pn
        elif (px != None and py != None and pn != None):
            self.name = pn
            self.x = px
            self.y = py
        else:
        # 完全不指定輸入變數
        # all arguments are None
            self.name = ""
            self.x = 0.0
            self.y = 0.0

p2 = Point(px=4, py=5, pn="這是點物件")
p3 = Point(pn="直接用點物件定義點", A=p2)
print(p2.x, p2.y, p2.name, p3.x, p3.y, p3.name)
p1 = Point(px=0, py=5, pn="指定點的 x 與 y 座標")
print(p1.x, p1.y, p1.name)
p4 =Point(A=p3, pn="這是 p4 點")
print(p4.name, p4.x, p4.y)

# Pythonic way to argument overloading
def sum(*summands):
    result = 0
    for summand in summands:
        result += summand
    return result
print(sum(1, 2, 3, 4))
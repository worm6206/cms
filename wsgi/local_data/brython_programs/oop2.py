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
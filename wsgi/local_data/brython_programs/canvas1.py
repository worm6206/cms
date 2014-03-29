#coding: utf-8
from math import *
import time
import random
# 準備繪圖畫布
canvas = doc["plotarea"]
ctx = canvas.getContext("2d")
# 定義座標轉換(0, 0) 到 (75, 20)
def change_ref_system(x, y):
    return (20 + x * 8, 420 - y * 20)
# 定義畫線函式
def draw_line(x1, y1, x2, y2, linethick = 3, color = "black"):
    ctx.beginPath()
    ctx.lineWidth = linethick
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.strokeStyle = color
    ctx.stroke()
# 定義一個點類別
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distanceTo(self, obj):
        if isinstance(obj, Point):
            return sqrt(pow(obj.x - self.x, 2) + pow(obj.y- self.y, 2))
        else:
            raise TypeError("Invalid type in Point.distanceTo()")
# 定義一個線類別
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # 定義一個 Line 的屬性 length
        self.length = self.p1.distanceTo(self.p2)
        self.deg = pi/180
    def rotate(self, angle):
        # 以 p1  為旋轉中心點
        # angle 為右手則旋轉角度
        # 這裡以左上角為原點, x 向右為正, y 向下為正
        self.p2.x = self.p1.x + self.length*cos(angle*self.deg)
        self.p2.y = self.p1.y - self.length*sin(angle*self.deg)
# 定義一個回呼繪圖函式
dataset = []
def graph():
    p1 = Point(0, 0)
    p2 = Point(10, 0)
    data = random.random() * 20
    doc["dataarea"] <= '%s, ' % str(data)[0:5]
    dataset.append(data)
    if len(dataset) == 1:
        x, y = change_ref_system(len(dataset), data)
        draw_line(x, y, x, y, linethick=3, color="blue")
    else:
        x1, y1 = change_ref_system(len(dataset)-1, dataset[-2])
        x2, y2 = change_ref_system(len(dataset), data)
        draw_line(x1, y1, x2, y2, linethick=3, color="blue")
    if len(dataset) >= 100:
        print(len(dataset))
        time.clear_interval(work)
p1 = Point(0, 0)
p2 = Point(10, 0)
p3 = Point(6.5, 7.8)
print("點 p1 到點 p2 的距離:", p1.distanceTo(p2))
line1 = Line(p1, p2)
print("線 line1 的長度:", line1.length)
# 以 p3 為圓心, 旋轉 90 度
line1.rotate(90)
#work = time.set_interval(graph, 100)
print("旋轉後, line1 的長度:", line1.length)
print("旋轉後, p1 的座標:", line1.p1.x, ",", line1.p1.y)
print("旋轉後, p2 的座標:", line1.p2.x, ",",  line1.p2.y)
x1, y1 = change_ref_system(0, 0)
for 索引 in range(0, 70, 4):
    x2, y2 = change_ref_system(索引, 20)
    draw_line(x1, y1, x2, y2, linethick=3, color="blue")
x1, y1 = change_ref_system(70, 0)
for 索引 in range(0, 70, 4):
    x2, y2 = change_ref_system(索引, 20)
    draw_line(x1, y1, x2, y2, linethick=3, color="red")
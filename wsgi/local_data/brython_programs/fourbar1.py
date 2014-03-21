# need yen_fourbar.js
from javascript import JSConstructor
import math
from browser import doc
import browser.timer
 
# convert Javascript function object into Brython object
point = JSConstructor(Point)
line = JSConstructor(Line)
link = JSConstructor(Link)
triangle = JSConstructor(Triangle)
 
def draw():
    global theta
    # clear canvas context
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    # draw linkeage
    line1.drawMe(ctx)
    line2.drawMe(ctx)
    line3.drawMe(ctx)
    # draw triangles
    #triangle1.drawMe(ctx)
    #triangle2.drawMe(ctx)
    # input link rotation increment
    theta += dx
    # calculate new p2 position according to new theta angle
    p2.x = p1.x + line1.length*math.cos(theta*degree)
    p2.y = p1.y - line1.length*math.sin(theta*degree)
    temp = triangle2.setPPSS(p2, p4, link3_len, link2_len)
    p3.x = temp[0]
    p3.y = temp[1]
 
 
x, y, r = 10, 10, 10
# define canvas and context
canvas = doc["plotarea"]
ctx = canvas.getContext("2d")
# fourbar linkage inputs
theta = 0
degree = math.pi/180
dx = 2
dy = 4
p1 = point(150, 100)
p2 = point(150, 200)
p3 = point(300, 300)
p4 = point(350, 100)
line1 = link(p1, p2)
line2 = link(p2, p3)
line3 = link(p3, p4)
line4 = link(p1, p4)
line5 = link(p2, p4)
link2_len = p2.distance(p3)
link3_len = p3.distance(p4)
triangle1 = triangle(p1,p2,p4)
triangle2 = triangle(p2,p3,p4)
temp = []
ctx.translate(0, canvas.height)
ctx.scale(1, -1)
browser.timer.set_interval(draw, 10)
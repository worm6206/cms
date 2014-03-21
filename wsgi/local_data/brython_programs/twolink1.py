#import Cango2D
from javascript import JSConstructor
from javascript import JSObject
 
cango = JSConstructor(Cango2D)
shapes2d = JSObject(shapes2D)
tweener = JSConstructor(Tweener)
cgo = cango("plotarea")
 
#cgo = Cango2D.cango("plotarea")
cgo.setWorldCoords(-50, -50, 200)
# 加上基軸與第一桿
# 畫筆移到 -20, -10, 畫直線到 -10,-10 以及 -10,0 
standData = ['M', -20,-10, 'L', -10,-10, -10,0, 'A', 10,10,0,0,1,10,0, 'L',10,-10, 20,-10, 20,-40, -20,-40,'z']
stand = cgo.compileShape(standData, 'darkgray', "#222222", 1)
axle0 = cgo.compileShape(shapes2d.circle, 'gray', "#222222", 10)
armGrp = cgo.createGroup2D(stand, axle0)
#cgo.render(armGrp)
segData = ['M',0,-8, 'A',8,8,0,0,1,0,8, 'L',50,8, 'A',8,8,0,0,1,50,-8, 'Z']
seg1 = cgo.compileShape(segData, 'darkGray', "#222222")
# 利用 zIndex 決定疊層的先後次序
seg1.zIndex = -1
axle1 = cgo.compileShape(shapes2d.circle, 'gray', "#222222", 8)
axle1.translate(50, 0)
axle1.zIndex = 1
seg1Grp = cgo.createGroup2D(seg1, axle1)
twn1 = tweener([0, 80, 45, 0], 0, 3500, 'loop')
seg1Grp.animateTransform.rotate(twn1)
armGrp.addObj(seg1Grp)
# 加上第二軸
seg2 = cgo.compileShape(segData, 'darkGray', "#222222")
seg2.zIndex = -1
axle2 = cgo.compileShape(shapes2d.circle, 'gray', "#222222", 8)
axle2.zIndex = 1
axle2.translate(50, 0)
 
seg2Grp = cgo.createGroup2D(seg2, axle2)
seg2Grp.animateTransform.translate(50,0)
twn2 = tweener([0, -60, -60, 0], 0, 3500, 'loop')
seg2Grp.animateTransform.rotate(twn2)
# 請注意 seg2Grp 加上 seg1Grp 物件上
seg1Grp.addObj(seg2Grp)
cgo.animate(armGrp)
cgo.playAnimation()
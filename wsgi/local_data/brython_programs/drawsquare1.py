from javascript import JSConstructor
from javascript import JSObject
import math
 
cango = JSConstructor(Cango2D)
#shapes2d = JSObject(shapes2D)
#tweener = JSConstructor(Tweener)
#drag2d = JSConstructor(Drag2D)
#svgtocgo2d = JSConstructor(svgToCgo2D)
#involutebezcoeffs = JSConstructor(involuteBezCoeffs)
#creategeartooth = JSConstructor(createGearTooth)
#createintgeartooth= JSConstructor(createIntGearTooth)

g = cango("plotarea")

g.setWorldCoords(-30, 30, -30, 50)
# path 會自動連接頭與尾
繪圖路徑 = ["M", 0, 0, "L", 10, 0, "L", 10, 10, "L", 0, 10, "z"]
scale = 10
正方形 = g.compilePath(繪圖路徑, 'blue', scale)
複製正方形 = 正方形.dup()
數量 = 7
for i in range(1, 數量+1):
    替身 = 複製正方形.dup()
    替身.rotate(360*i/數量)
    複製正方形.appendPath(替身, true)
複製正方形.translate(250,250)
g.render(複製正方形)
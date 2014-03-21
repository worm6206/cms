from javascript import JSConstructor
from javascript import JSObject
 
cango = JSConstructor(Cango2D)
shapes2d = JSObject(shapes2D)
tweener = JSConstructor(Tweener)
cgo = cango("plotarea")

rect = ["M", 0, 100, 500, 100, 500, 200, 0, 200, "z"]
bkg = cgo.drawShape(rect, 0, 100,'red')
tri = cgo.compileShape(shapes2d.triangle, 'black', 'black')
tri.scale(300);
hole = cgo.compileShape(shapes2d.circle, 'red', 'red')
hole.scale(250)
hole.translate(200, 200)
tri.translate(200,200)
tri.appendPath(hole)
cgo.render(tri)
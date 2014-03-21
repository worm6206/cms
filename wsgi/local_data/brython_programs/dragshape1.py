from javascript import JSConstructor
from javascript import JSObject
 
cango = JSConstructor(Cango2D)
shapes2d = JSObject(shapes2D)
tweener = JSConstructor(Tweener)
drag2d = JSConstructor(Drag2D)
svgtocgo2d = JSConstructor(svgToCgo2D)
cgo = cango("plotarea")

def dragBox():
    x1, y1, w, h = 80, 10, 40, 100
    boxOutline = ['M', 0, 0, 'l', w, 0, 0, h, -w, 0, 'z']

    def dragB1(mousePos):
        global x, y
        wPos = cgo.toWorldCoords(mousePos.x , mousePos.y)
        x = wPos.x
        y = wPos.y
        box.transform.reset()
        box.transform.translate(x, y)
        cgo.renderFrame(box)

    drag = drag2d(cgo, null, dragB1, null)
    cgo.clearCanvas()
    cgo.setWorldCoords(-100, -100, 400)
    box = cgo.compileShape(boxOutline, 'orange', "#222222", 1)
    box.enableDrag(drag)
    box.rotate(-85)
    box.translate(x1, y1)
    cgo.render(box)

dragBox()

from javascript import JSConstructor
from javascript import JSObject
 
cango = JSConstructor(Cango2D)
shapes2d = JSObject(shapes2D)
tweener = JSConstructor(Tweener)
cgo = cango("plotarea")
cgo.setWorldCoords(-5, -5, 20);
hullo = cgo.drawText("Hello World", 5, 3, "blue", 18, 5);
xTwn = tweener([5,0], 0, 2000);
rotTwn = tweener([0,360], 0, 2000);
hullo.animateTransform.translate(xTwn);
hullo.animateTransform.rotate(rotTwn);

cgo.animate(hullo);
cgo.playAnimation();
from browser import html
from javascript import JSConstructor

# create an new canvas called new_canvas
canvas = html.CANVAS()
canvas.height = 800
canvas.width = 600
canvas.id = "new_canvas"
doc <= canvas

# use new_canvas to load stl part
stlviewer = JSConstructor(STLViewer)
stlviewer("/downloads/spikeball.stl", "new_canvas")

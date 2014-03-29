import math

# 準備在 id="plotarea" 的 canvas 中繪圖
canvas = doc["plotarea"]
ctx = canvas.getContext("2d")
''' can not fully clear Canvas unless reload the page?
ctx.save()
ctx.setTransform(1, 0, 0, 1, 0, 0)
ctx.clearRect(0, 0, canvas.width, canvas.height)
ctx.restore()
'''
ctx.beginPath()
ctx.lineWidth = 3
ctx.moveTo(0, 0)
ctx.lineTo(0, 500)
ctx.strokeStyle = "red"
ctx.stroke()

ctx.beginPath()
ctx.lineWidth = 3
ctx.moveTo(0, 0)
ctx.lineTo(500, 0)
ctx.strokeStyle = "blue"
ctx.stroke()

ctx.beginPath()
ctx.lineWidth = 3
ctx.moveTo(0, 0)
ctx.lineTo(500, 500)
ctx.strokeStyle = "green"
ctx.stroke()

ctx.beginPath()
ctx.lineWidth = 3
ctx.strokeStyle = "black"
ctx.arc(250,250,50,0,2*math.pi)
ctx.stroke()
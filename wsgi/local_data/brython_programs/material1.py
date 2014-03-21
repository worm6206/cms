#coding: utf8
# 參考: http://www.engineersedge.com/calculators/section_square_case_11.htm
import math
# 實心圓棒斷面性質計算
直徑 = 1
# pi 與 e 屬於 math 模組(類別)屬性
轉動慣性矩 = math.pi*直徑**4/64
截面模數 = math.pi*直徑**3/32
迴轉半徑 = 直徑/4
截面積 = math.pi*(直徑/2)**2
print(轉動慣性矩)
print(截面模數)
print(截面積)
# 利用 round() 取到小數點 3 位數
print(round(轉動慣性矩, 3))
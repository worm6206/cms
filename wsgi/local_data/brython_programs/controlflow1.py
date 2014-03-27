#coding: utf-8
'''
program: controlflow1.py
'''

# 建立數列
numbers = [22, 34, 12, 32, 4]
# 設定初始值
sum = 0
# 取得數列長度
i = len(numbers)

# 以逐次減一方式重複迴圈
while (i != 0):
    i -= 1
    sum = sum + numbers[i]

print("The sum is: ", sum)

'''
利用 break 中斷迴圈執行
'''
import random

while (True):
    val = random.randint(1, 30)
    print(val)
    if (val ==  22):
       break
'''
利用 continue 中止執行迴圈其他內容
'''
num = 0

while (num < 30):
    num = num + 1
    if (num % 2) == 0:
       continue
    print("只會印出奇數:", num)
   
'''
if 判斷式
'''
age = 17

if age > 18:
    print("可以考駕照!")
else:
    print("還不能考駕照!")

name = "Luke"

if name == "Jack":
   print("Hello Jack!")
elif name == "John":
   print("Hello John!")
elif name == "Luke":
   print("Hello Luke!")
else:
   print("Hello there!")
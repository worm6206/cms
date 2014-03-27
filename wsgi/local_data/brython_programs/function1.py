# sum.py
# Allow     sum(n) to add [1, 2, 3, ... n]
#	or	sum(a, n) to add [a, a+1, ..., n]
def sum(*args):
    if len(args) == 1:
        start = 1
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]
    s = 0
    for x in range(start, stop+1):
        s += x
    return s

print(sum(10))
print(sum(3, 4))

'''
lambda 使用
'''

def root(x):
   return x * x

a = root(2)
b = root(15)

print(a, b)

# 以下使用 lambda

for i in (1, 4, 3, 2, 15):
   a =  lambda x: x * x
   print(a(i))

'''
全域變數使用, 注意 function1 與 function2 差異
'''

x = 15

def function1():
    x = 45
   
def function2():
    global x
    x = 45

function1()
print(x)
function2()
print(x)
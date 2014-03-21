資料 = [1, 2, 3, 4, 5]

'''
有關此程式的用法
'''
print(資料[:3])
print(資料[2:])
print(資料[1:2])

a = [3, 5, 7, 11, 13]
for x in a:
    if x == 7:
        print('list contains 7')
        break
print(list(range(10)))

for 索引 in range(-5, 6, 2):
    print(索引)

squares = [ x*x for x in range(0, 11) ]
print(squares)

a = [10, 'sage', 3.14159]
b = a[:]
#list.pop([i])    取出 list 中索引值為 i 的元素，預設是最後一個
print(b.pop())
print(a)

數列 = [0]*10
print(數列)

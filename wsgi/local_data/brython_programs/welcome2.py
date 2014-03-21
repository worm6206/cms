#encoding: utf-8

print("歡迎學習 Python3 程式")

for 索引 in range(5):
    print("歡迎學習 Python3 程式")

for 索引 in range(5):
    print("歡迎學習 Python3 程式", end="")

# 以下用來列印金字塔
# 第一步
print("\n1***********************************")
print("開始學程式語言","*")
# 第二步
print("2***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言","*")
# 第三步
print("3***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言","*",end="")
# 第四步
print("4***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,10):
        print("*",end="")
    print("")
# 第五步
print("5***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(0,變數1):
        print("*",end="")
    print("")
# 第六步
print("6***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")

for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")
# 第七步
print("7***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")

for 變數1 in range(10,1,-1):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")
# 第八步
print("8***********************************")
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")

#因為終點 1, 沒有辦法列印出一個星號, 因此將步驟 7 的 1 改為 0, 讓迴圈多印一行
for 變數1 in range(10,0,-1):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")
# 第九步
print("9***********************************")
'''
設法利用函式的定義與呼叫, 將重複的部分予以整合, 也順便擴大程式的適用範圍
目的:
1. 不是只能印出最多 9 個星號, 而是可以隨輸入而改變, 以增加程式的彈性
2. 不是只能印出"開始學程式語言", 而是可以隨輸入而改變, 列印程式使用者所輸入的字串, 以增加程式的彈性
3. 函式定義的部分 (注意冒號與縮排)
def function(input_variable):
    print("程式內容")
4. 函式呼叫的部分
function(input_variable)
'''
# 將第一部分列印的 10 取出, 以 num 取代, 將 num 當作函式的輸入變數
def firstPrint(num):
    for 變數1 in range(1,num):
        print("開始學程式語言",end="")
        for 變數2 in range(1,變數1+1):
            print("*",end="")
        print("")

# 測試一下 firstPrint(num) 函式的呼叫
firstPrint(10)
'''
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")
'''
#因為終點 1, 沒有辦法列印出一個星號, 因此將步驟 7 的 1 改為 0, 讓迴圈多印一行,且是列印一個星號
for 變數1 in range(10,0,-1):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")
# 第十步
print("10***********************************")
'''
設法利用函式的定義與呼叫, 將重複的部分予以整合, 也順便擴大程式的適用範圍
目的:
1. 不是只能印出最多 9 個星號, 而是可以隨輸入而改變, 以增加程式的彈性
2. 不是只能印出"開始學程式語言", 而是可以隨輸入而改變, 列印程式使用者所輸入的字串, 以增加程式的彈性
3. 函式定義的部分 (注意冒號與縮排)
def function(input_variable):
    print("程式內容")
4. 函式呼叫的部分
function(input_variable)
'''
# 將第一部分列印的 10 取出, 以 num 取代, 將 num 當作函式的輸入變數
# 將字串列印部分, 也取出, 以 string 取代, 將 string 當作函式的輸入變數
def firstPrint(string,num):
    for 變數1 in range(1,num):
        #print("開始學程式語言",end="")
        # 以 string 取代"開始學程式語言"
        print(string,end="")
        for 變數2 in range(1,變數1+1):
            print("*",end="")
        print("")

# 測試一下 firstPrint(num) 函式的呼叫
# 函式定義修改後, 函式的呼叫也要配合修改, 目前德 firstPrint() 需要兩個輸入變數, 第一個為字串, 第二個為數字
firstPrint("我的輸入字串",10)
'''
for 變數1 in range(1,10):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")
'''
#因為終點 1, 沒有辦法列印出一個星號, 因此將步驟 7 的 1 改為 0, 讓迴圈多印一行,且是列印一個星號
for 變數1 in range(10,0,-1):
    print("開始學程式語言",end="")
    for 變數2 in range(1,變數1+1):
        print("*",end="")
    print("")

######################################
# 十步之後完成的程式
print("*****終於完成 Python3 學習的第一階段*****")
'''
printC(num): 輸入num, 列印num個星號, 並且不跳行
'''
def printC(num):
    for i in range(0,num):
      print("*",end="")
      
'''
printS(string,i): 輸入string與i, 列印string, 並且不跳行, 接著列印i個星號, 最後跳行
'''
def printS(string,i):
    print(string,end="")
    printC(i)
    print("")

'''
triangle(string,num): 輸入string與num, 以 num 為三角形最高點, 先漸增再漸減
'''
def triangle(string,num):
    for i in range(1,num+1):
        '''
        print(string,end="")
        printC(i)
        print("")
        '''
        printS(string,i)
    for i in range(num-1,0,-1):
        #print(string,end="")
        #printC(i)
        #print("")
        printS(string,i)
        
triangle("開始學Python",10)
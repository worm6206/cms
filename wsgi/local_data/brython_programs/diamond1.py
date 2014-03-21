def 列印星號(輸入變數):
    數列1 = list(range(輸入變數))
    數列2 = [x+輸入變數-1 for x in 數列1]
    反數列2 = reversed(數列1)
    集合 = zip(數列2, 反數列2)
    for 索引 in 集合:
        for 數 in range(輸入變數*2):
            if 數 == 索引[0] or 數 == 索引[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def 列印星號2(輸入變數):
    數列1 = list(range(輸入變數))
    數列2 = [x+輸入變數 for x in 數列1]
    數列3 = [x+1 for x in 數列1]
    反數列2 = reversed(數列2)
    集合 = zip(數列3, 反數列2)
    for 索引 in 集合:
        for 數 in range(輸入變數*2):
            if 數 == 索引[0] or 數 == 索引[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def 列印菱形(輸入變數):
    列印星號(輸入變數)
    列印星號2(輸入變數-1)

列印菱形(15)
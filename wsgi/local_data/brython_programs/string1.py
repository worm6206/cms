for 索引 in range(5):
    print(索引, "列印字串")
    
lyrics = """\
Are you really here or am I dreaming
I can't tell dreams from truth 
for it's been so long since I have seen you
I can hardly remember your face anymore 
"""

for i in lyrics:
    # 每一行的列印都不要有跳行符號
    print(i, end="")
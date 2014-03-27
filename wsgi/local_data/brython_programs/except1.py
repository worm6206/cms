'''
利用 ajax 讀取伺服器上的檔案
例如: /downloads/
/images/
/brython_programs/ 目錄下的檔案
'''

f = None

try:
    f = open('/brython_programs/function1.py', 'r')
    for i in f:
        print(i)
except IOError:
    print("Error reading file")
finally:
    if f:
        f.close()
        
'''
raise 與客製化 exception
'''

class YesNoException(Exception):
    def __init__(self):
       print('印出 Invalid value')


answer = 'y'

if (answer != 'yes' and answer != 'no'):
    raise YesNoException()
else:
    print('Correct value')
from browser import doc, alert, html

def echo(ev):
    alert(doc["input_zone"].value)

# 在設定物件連結之前, 要先有物件設定, 因此將 button 放在這裡
doc <= html.BUTTON("顯示 alert 的按鈕", id="alert_button")

# 連結 alert_button 與 echo 函式, 按下按鈕會執行 echo 函式
doc['alert_button'].bind('click',echo)
# 顯示輸入欄位
doc <= html.BR() + '輸入:' + html.INPUT(id='input_zone')

# 多重選項
items = ['one', 'two', 'three']
sel = html.SELECT()
for i, elt in enumerate(items):
    sel <= html.OPTION(elt, value = i)
doc <= sel

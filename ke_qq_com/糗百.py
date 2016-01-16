#coding:utf-8
from Tkinter import *   #引用Tk模块
import urllib2,re
root = Tk()             #初始化Tk()
root.title("糗事百科桌面版")
root.geometry('500x400')                 #是x 不是*
txt=Text(root,font=("黑体",20))
page=1
indexxx=0
def getText():
    qiubai="http://www.qiushibaike.com/textnew/page/"+str(page)
    top={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    html=urllib2.Request(qiubai,headers=top)
    html=urllib2.urlopen(html).read()
    reg=r'<div class="content">([\s\S]+?)<!--.+?-->'
    reg=re.compile(reg)
    text=re.findall(reg,html)
    return text

def showText():
    if page==1:
        msg=getText()
        page+=1
        txt.delete(1.0,END)
        txt.insert(1.0,msg[indexxx])
        indexxx+=1
        global  indexxx
        global msg
        global page
    else:
        if indexxx==19:
            indexxx=0
            page+=1
            msg=getText()
            txt.delete(1.0,END)
            txt.insert(1.0,msg[indexxx])
            indexxx+=1
        else:
            txt.delete(1.0,END)
            txt.insert(1.0,msg[indexxx])
            indexxx+=1
        global  indexxx

btn=Button(root,text="下一条",width=50,command=showText).pack(side=BOTTOM)
txt.pack()
root.mainloop()
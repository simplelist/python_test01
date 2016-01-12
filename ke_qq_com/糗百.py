#coding:utf-8
from Tkinter import *   #引用Tk模块
root = Tk()             #初始化Tk()
root.title("糗事百科桌面版")
root.geometry('500x400')                 #是x 不是*
txt=Text(root,font=("黑体",20))
def showText():
    txt.delete(1.0,END)
    txt.insert(1.0,"qqqq")
btn=Button(root,text="下一条",width=50,command=showText).pack(side=BOTTOM)
txt.pack()
root.mainloop()
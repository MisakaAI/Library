# -*- coding: utf-8 -*-
# 消息提醒
# 用于弹出一个窗口进行消息提醒，适用分辨率1920×1080
# .pyw 用 pythonw.exe 运行，没有控制台

import sys
import tkinter

def talk(text,autoclose=None):
    def close(x=None):
        baseFrame.destroy()
    baseFrame = tkinter.Tk()
    baseFrame.configure(background="#000000")
    baseFrame.resizable(width=False, height=False)
    baseFrame.overrideredirect(True)
    baseFrame.attributes('-topmost',1)
    sw = baseFrame.winfo_screenwidth()
    sh = baseFrame.winfo_screenheight()
    ww = 1920
    wh = 100
    x = (sw-ww) / 2
    y = (sh-wh) / 2
    baseFrame.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
    lb = tkinter.Label(baseFrame,
                   text=text,
                   background="#000000",
                   foreground='red',
                   font=('Microsoft YaHei',50)
                   )
    lb.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)
    baseFrame.bind('<Button-1>', close)
    baseFrame.attributes("-alpha",0.8)
    if autoclose != None:
        baseFrame.after(autoclose, close)
    baseFrame.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        talk(sys.argv[1])
    else:
        talk('?')

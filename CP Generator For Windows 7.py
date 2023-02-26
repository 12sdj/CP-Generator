#!/user/bin/env python
# -*- coding:utf-8 -*-
# @software: Visual Studio Code
from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import tkinter as tk
import ctypes
import webbrowser
import time
import threading
from ttkthemes import*
from time import strftime
import winsound
import socket
import getpass
import os
import sys
from tkinter.scrolledtext import ScrolledText
#root=Tk()
root=ThemedTk(theme="adapta", toplevel=True, themebg=True)
winWidth = 720
winHeight = 480
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
root.geometry(f"{winWidth}x{winHeight}+{x}+{y}")
root.title("CP Generator For Windows 7")
root.resizable(0,0)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)#>=win8.1
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()#<win8.1
#ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
#root.tk.call('tk', 'scaling', ScaleFactor/75)
#----------------------------------------------------------
global f
f = 1
global e
e = 50
global numset
numset = 1
global end_control



#####-------------------------------------------------------------------------
#####----------------------------------------------------------------MAIN UNIT!!!!!!
# #98D2E4
# #FF6A00
# #006DDA


state_1 = Text(root, relief="flat", font=("Microsoft YaHei UI", 80))
state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
label_b = Label(root,
                   text='x',
                   font=("Microsoft YaHei UI", 80))


label_b.place(relx=0.45, y=100, relwidth=0.15, height=400)
state_3 = Text(root, relief="flat", font=("Microsoft YaHei UI", 80))
state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
state_1.configure(state='disabled')
state_3.configure(state='disabled')

####__________________________________________________________BETA
class Job(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.01)
            global number_1
            try:
                number_1 = randint(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n")
                t1.pause()
            state_1.delete('0.0', END)
            state_1.insert(INSERT, number_1)
            #print("1")
    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False    
class hello(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            time.sleep(0.01)
            global number_3
            try:
                number_3 = randint(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n")
                t3.pause()
            state_3.delete('0.0', END)
            state_3.insert(INSERT, number_3)
            #print("3")
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       

def thread_4(func):
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    
threads = []
t1 = Job()
t3 = hello()
t4 = threading.Thread(target=thread_4,args=(u'thread_state_4',))
threads.append(t1)
t1.pause()
threads.append(t3)
t3.pause()
threads.append(t4)
if __name__ == '__main__':
    for t in threads:
        t.daemon=True
        #t.setDaemon(True) #被t.daemon=True替代(python 3.10)
        t.start()


#-----------------------------------------------------
def control():
    control['state'] = DISABLED
    end['state'] = NORMAL
    setting['state'] = DISABLED
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n")
    state.insert(INSERT, "您可以点击“停止运行”进行查看\n")
    state.insert(INSERT, "当前设定值： ")
    state.insert(INSERT, f)
    state.insert(INSERT, " <-> ")
    state.insert(INSERT, e)
    state.configure(state='disabled')
    state_1.configure(state='normal')
    state_3.configure(state='normal')
    t1.resume()
    t3.resume()
    #message = "The Random Number Is "+ str(number_1)
    #control_info = showinfo(title='INFO',message=message)
def end():  # sourcery skip: avoid-builtin-shadow
    control['state'] = NORMAL
    end['state'] = DISABLED
    setting['state'] = NORMAL

    list=[]
    for _ in range(100):
        r = randint(f,e)
        if r not in list: list.append(r)
    try:
        number_a = list[0]
        number_b = list[1]
        number_c = list[2]
    except Exception:
        number_a = randint(f,e)
        number_b = randint(f,e)
        number_c = randint(f,e)

    #L1 = sample(range(f, e), 5)
    #print(L1)

    state_1.delete('0.0', END)
    state_1.insert(INSERT, number_a)
    state_3.delete('0.0', END)
    state_3.insert(INSERT, number_c)



    state_1.configure(state='disabled')
    state_3.configure(state='disabled')
    t1.pause()
    t3.pause()
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：空闲\n")
    state.insert(INSERT, "您可以在设置参数后点击“开始运行”产生随机数")
    state.configure(state='disabled')
#-----------------------------------------------------
def minimize():
    root.iconify()
def showPopupMenu(event):
    rightmenu.post(event.x_root,event.y_root)
##---------------------------------------------------
def t_close_handler_about():
    root.attributes('-disabled', 0)
    window_about.destroy()
def about():
    
    def update():
        webbrowser.open('https://github.com/12sdj/CP-Generator')
    global window_about
    window_about = Toplevel(root)
    window_about.geometry("680x340+200+250")
    window_about.resizable(0,0)
    window_about.attributes('-toolwindow', True)
    window_about.title("About")
    #window_about.mainloop()
    window_about.protocol("WM_DELETE_WINDOW", t_close_handler_about)
    root.attributes('-disabled', 1)
    #Unint
    label_a = Label(window_about,
                   text='About',
                   font=("Microsoft YaHei UI", 12))
    label_a.pack()
    tip_window = Label(window_about,
                    text='CP Generator For Windows 7\n'
                            'Version 1.0.0_Release\n'
                            '2023/2/25 (UTC+8) Update 1\n'
                            'Copyright (c) 2023 12sdj [Copyright Reserved only]',
                    font=("Microsoft YaHei UI", 10),
                    foreground="black")
    tip_window.pack()
    control2 = Button(window_about, text ="访问程序在Github上的页面", command = update)
    control2.pack(side=BOTTOM)
##----------------------------------------------------


##----------------------------------------------------    
def t_close_handler_setting():
    root.attributes('-disabled', 0)
    window_setting.destroy()
def setting():  # sourcery skip: avoid-builtin-shadow
    global num
    num = 1

    def func(*args):
        pass

    def funk(*args):
        pass

    def chosen():
        global numset
        numset = var.get()


    def application():
        global f
        global e
        global numset
        try:

            f = float(label_b_1.get())
            e = float(label_b_3.get())

                #####
            if f >= e:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（前一个控件的值不能大于或等于后一个控件的值）\n建议更改后再次检查设置\n")
                control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用CP Generator!\n")
                f = 1
                e = 50
                label_b_1.delete(0, "end")
                label_b_1.insert(0, f)
                label_b_3.delete(0, "end")
                label_b_3.insert(0, e)
            if f <= 0 or e <= 0 or f % 1 != 0 or e % 1 != 0 or f <= 0.0 or e <= 0.0 or f % 1 != 0.0 or e % 1 != 0.0:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n")
                control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用CP Generator!\n")
                f = 1
                e = 50
                label_b_1.delete(0, "end")
                label_b_1.insert(0, f)
                label_b_3.delete(0, "end")
                label_b_3.insert(0, e)
            else:
                f = int(label_b_1.get())
                e = int(label_b_3.get())
                control_info = showinfo(title='Program Info',message="没有发现原则性错误。\n程序经过检查，发现你的设置没有原则性错误，你可以正常使用CP Generator!\n")

        except Exception:
            f = str(label_b_1.get())
            e = str(label_b_3.get())

            if not f or not e:
                control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个输入框不能为空，请填写符合您配置的值）。\n建议更改后再次检查设置\n")
                control_info = showinfo(title='Program Info',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用CP Generator!\n")
                f = 1
                e = 50
                label_b_1.delete(0, "end")
                label_b_1.insert(0, f)
                label_b_3.delete(0, "end")
                label_b_3.insert(0, e)
            else:
                s=str(f).split('.')
                s1=str(e).split('.')
                try:
                    f = float(label_b_1.get())
                    e = float(label_b_3.get())
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n")
                    control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用CP Generator!\n")
                    f = 1
                    e = 50
                    label_b_1.delete(0, "end")
                    label_b_1.insert(0, f)
                    label_b_3.delete(0, "end")
                    label_b_3.insert(0, e)
                except Exception:
                    control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（输入的值必须是一个有理数）。\n建议更改后再次检查设置\n")
                    control_info = showinfo(title='Program Info',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用CP Generator!\n")
                    f = 1
                    e = 50
                    label_b_1.delete(0, "end")
                    label_b_1.insert(0, f)
                    label_b_3.delete(0, "end")
                    label_b_3.insert(0, e)

                

    def application2():
        global numset
        numset = 1
        global f,e
        var.set(1)

        f = 1
        e = 50
        label_b_1.delete(0, "end")
        label_b_1.insert(0, f)
        label_b_3.delete(0, "end")
        label_b_3.insert(0, e)
        
        control_info = showinfo(title='Program Info',message="已恢复CP Generator默认设置\n")



    global window_setting
    window_setting = Toplevel(root)
    window_setting.geometry("850x600+350+550")
    window_setting.resizable(0,0)
    #window_setting.attributes('-toolwindow', True)
    window_setting.protocol("WM_DELETE_WINDOW", t_close_handler_setting)
    window_setting.title("Control Panel")
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_setting,
                   text='程序设置',
                   font=("Microsoft YaHei UI", 15))
    label_b.pack()    





    label_b = Label(window_setting,
                   text='生成类型',
                   font=("Microsoft YaHei UI", 12))
    label_b.place(relx=0.01, y=40, relwidth=0.3, height=30)

    var = IntVar()
    var.set(numset)
    b = Radiobutton(window_setting,text="范围内任意学号",variable = var ,value =1,command=chosen)
    b.place(relx=0.01, y=70, relwidth=0.24, height=40)
    b3 = Radiobutton(window_setting,text="男女配对",variable = var ,value =2,command=chosen, state=DISABLED)
    b3.place(relx=0.01, y=110, relwidth=0.24, height=40)
    
    label_b = Label(window_setting,
                   text='范围',
                   font=("Microsoft YaHei UI", 12))


    label_b.place(relx=0.01, y=150, relwidth=0.1, height=40)
    label_b_1 = Entry(window_setting, font=("Microsoft YaHei UI", 14),background='gray')
    label_b_1.place(relx=0.01, y=190, relwidth=0.15, height=40)
    label_b_2 = Label(window_setting,text = '-', font=("Microsoft YaHei UI", 16))
    label_b_2.place(relx=0.17, y=190, relwidth=0.02, height=40)
    label_b_3 = Entry(window_setting, font=("Microsoft YaHei UI", 14),background='gray')
    label_b_3.place(relx=0.2, y=190, relwidth=0.15, height=40)

    label_b_1.delete(0, "end")
    label_b_1.insert(0, f)
    label_b_3.delete(0, "end")
    label_b_3.insert(0, e)


    text_b_1 = Label(window_setting,text = '选项说明', font=("Microsoft YaHei UI", 12))
    text_b_1.place(relx=0.5, y=40, relwidth=0.2, height=40)    
    text_b_2 = Label(window_setting,text = '范围内任意学号：\n运行程序后，在您设定的范围中随机挑选两个\n正整数，分别填写在主界面x的左边和右边\n运行结束后，可能会出现以下两种情况：\n NC（男x女）\n AC（男x男 或 女x女。前者被称为“攻”和“受”，\n后者被称为“顶”和“底”）\n\n男女配对：\n选择该选项后，您需要填写男生和女生各自的范围。\n程序运行后，有且仅有一种情况，即NC。\n该选项正处于研发阶段，暂时无法选择该选项。\n\n关于对CP的解释，来源于：https://zh.wikipe\ndia.org/zh-hans/%E9%85%8D%E5%B0%8\nD_(%E5%90%8C%E4%BA%BA)', font=("Microsoft YaHei UI", 10))
    text_b_2.place(relx=0.5, y=80, relwidth=0.49, height=430)    

    application = Button(window_setting,
                    text='检查并应用设置',
                    command=application)

    application.place(relx=0.02, y=560, relwidth=0.25, height=35)
    application2 = Button(window_setting,
                    text='恢复默认设置',
                    command=application2)

    application2.place(relx=0.27, y=560, relwidth=0.25, height=35)
    label_tip2 = Label(window_setting,
                   text='程序会根据您对程序的配置而运行',
                   font=("Microsoft YaHei UI", 9))
    label_tip2.place(relx=0.66, y=560, relwidth=0.32, height=35) 
    
##----------------------------------------------------    

#-----------------------------------------------------
def t_close_handler():
    root.attributes("-disabled", 0)
    window.destroy()
def status():
    def apply():
        alpha = scale.get()
        alpha = alpha / 100
        root.attributes('-alpha',alpha)
        acc = round(alpha,2)
        viewa = f"当前设定值:{str(acc)}"
                
            

    if demoStatus.get():
        global window
        window = Toplevel(root)
        window.geometry("620x300+200+250")
        window.title("透明效果设置")
        root.attributes('-alpha',0.85)
        tip2_window = Label(window,
                    text='透明效果\n',
                    font=("Microsoft YaHei UI", 12),
                    foreground="black")
        tip2_window.pack()
        scale = Scale(window, from_=10, to_=96,orient=HORIZONTAL,length=220)
        scale.set(85)
        scale.pack()

        root.attributes('-disabled', 1)#Top=window
        tip_window = Label(window,
                    text='提示：\n'
                    '通过拖动或点击滑动条设置主窗口透明度。\n'
                            '数值越小，透明程度越高；数值越大，则反之\n'
                            '建议的值为85-95之间，默认值为85',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
        tip_window.place(relx=0.05, y=120, relwidth=0.55, height=100)
        beta_window = Label(window,
                    text='Beta Setting\n ',
                    font=("Microsoft YaHei UI", 16),
                    foreground="black")
        beta_window.place(relx=0.65, y=170, relwidth=0.35, height=50)





        apply = Button(window,
                    text='应用',
                    command=apply)
        apply.place(relx=0.4, y=260, relwidth=0.2, height=35)
        window.resizable(0,0)
        window.attributes('-toolwindow', True)
        window.protocol("WM_DELETE_WINDOW", t_close_handler)
        #window.mainloop()

    else:
        root.attributes('-alpha',1)
def topview():
    if homoStatus.get():
        root.attributes('-topmost', -1)
    else:
       root.attributes('-topmost', 0)    

#-----------------------

#-----------------------



#-----------------------------------------------------
label_1 = Label(root,
                   text='CP Generator',
                   font=("Microsoft YaHei UI", 12))
label_1.pack()
label_2 = Label(root,
                   text='通知中心',
                   font=("Microsoft YaHei UI", 8))
label_2.place(relx=0.03, y=40, relwidth=0.45, height=25)
label_3 = Label(root,
                   text='控制台',
                   font=("Microsoft YaHei UI", 8))
label_3.place(relx=0.55, y=40, relwidth=0.45, height=25)
label_4 = Label(root,
                   text='输出',
                   font=("Microsoft YaHei UI", 8))
label_4.place(relx=0.03, y=195, relwidth=0.45, height=25)
state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
state.place(relx=0.03, y=70, relwidth=0.5, height=120)
state.insert(INSERT, "当前状态：空闲\n")
state.insert(INSERT, "您可以在设置参数后点击“开始运行”产生随机数")
state.configure(state='disabled')
#state.delete('0.0', END)
control = Button(root, text ="开始运行", command = control)
control.place(relx=0.55, y=70, relwidth=0.4, height=40)
end = Button(root, text ="停止运行", command = end)
end.place(relx=0.55, y=110, relwidth=0.4, height=40)
end['state'] = DISABLED
setting = Button(root, text ="设置", command = setting)
setting.place(relx=0.55, y=150, relwidth=0.4, height=40)


####----------------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label='关于', command=about)


winmenu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='窗口设置', menu=winmenu)
demoStatus = BooleanVar()
demoStatus.set(False)
homoStatus = BooleanVar()
homoStatus.set(False)
winmenu.add_checkbutton(label = "透明效果",command=status,variable=demoStatus)
winmenu.add_checkbutton(label = "窗口前置",command=topview,variable=homoStatus)
root.config(menu=menubar)
winmenu.add_separator()
winmenu.add_command(label='退出程序', command=root.quit)
    
    

#<Button - 3>
rightmenu = Menu(root,tearoff=False)
rightmenu.add_command(label="最小化窗口",command=minimize)
rightmenu.add_command(label="退出程序",command=root.destroy)
root.bind("<Button-3>",showPopupMenu)




root.mainloop()

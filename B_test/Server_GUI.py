# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: Server_GUI.py
 @function: 服务端界面程序，可以打开和传输文件的Server.py和下载文件的Server_def.py
 @author:  linxin
 @date:  7/8/2020 - 8:31 AM
'''

#

from tkinter import  *
from tkinter import messagebox
import Server
import  Server_def


# 创建窗口
login = Tk()
# 修改窗口名字
login.title('B测文件传输系统-服务端启动')
# 修改窗口大小尺寸和位置
login.geometry('300x200+500+300')

# 创建标题标签
lable = Label(login,text='B测文件传输系统-服务端启动',font=('Arial',12),width=15,height=2)
lable.pack()

def run_server():
    # 启动传输文件的通信Server()
    Server.Server()
    # 启动下载文件的通信Server_def()
    Server_def.Server_def()
    messagebox.showerror('Successful', 'Server启动完成！!')




# 创建登录按钮组件，同时设置按钮事件处理函数
btn_login = Button(login,text='Run',command=run_server)
btn_login.place(x=30, y=120, width=50, height=20)


# 显示窗口
mainloop()
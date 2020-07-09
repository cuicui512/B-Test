# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: loginGUI.py
 @function:登录界面GUI
 @author:  linxin
 @date:  7/6/2020 - 10:28 AM
'''

from tkinter import  *
from tkinter import messagebox
import  downloadGUI
import  pymysql_

# 创建窗口
login = Tk()
# 修改窗口名字
login.title('B测文件传输系统-登录')
# 修改窗口大小尺寸和位置
login.geometry('300x200+500+300')

# 创建标题标签
lable = Label(login,text='B测文件传输系统',font=('Arial',12),width=15,height=2)
lable.pack()

# 创建相关变量
user_id = StringVar()
user_id.set('')
password = StringVar()
password.set('')

# 创建输入框标签
label_id = Label(login, text='用户名:', justify=RIGHT, width=100)
# 将标签放到窗口上
label_id.place(x=10, y=50, width=100, height=20)
# 创建文本框，同时设置关联的变量
entry_id = Entry(login, width=100, textvariable=user_id)
entry_id.place(x=100, y=50, width=100, height=20)


label_password = Label(login, text='密 码:', justify=RIGHT, width=80)
label_password.place(x=10, y=80, width=100, height=20)
#创建密码文本框
entry_password = Entry(login, show='*',width=100, textvariable=password)
entry_password.place(x=100, y=80, width=100, height=20)

# 登录按钮事件处理函数,这个名字不要和前面的窗口名字重叠
def login_():
    # 获取用户名和密码
    name = entry_id.get()
    # print(name)
    pwd = entry_password.get()
    password = pymysql_.password(name)
    if pwd==password:
        messagebox.showinfo('Successful', '登录成功！')
        login.destroy() # 关闭当前窗口
        downloadGUI.main_GUI() # 打开主窗口
    else:
        messagebox.showerror('Failed', '登录失败!')
# 定义函数，清空输入框
def cancel():
# 清空用户输入的用户名和密码
    user_id.set('')
    password.set('')


# 创建登录按钮组件，同时设置按钮事件处理函数
btn_login = Button(login,text='Login',command = login_)
btn_login.place(x=30, y=120, width=50, height=20)

# 创建登录按钮组件，同时设置按钮事件处理函数
btn_cancle = Button(login,text='Clear',command = cancel)
btn_cancle.place(x=150, y=120, width=50, height=20)

# 显示窗口
mainloop()
# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: downloadGUI.py
 @function: 下载的GUI程序
 @author:  linxin
 @date:  7/5/2020 - 3:17 PM
'''
from tkinter import ttk
from tkinter import  *
# 用于选择文件
from tkinter import filedialog
from tkinter import messagebox

import time
import datetime
import os
import Client_def
import pymysql_
import  Client_
import  Client_def
import  disk_size

# 连接mysql数据库



# 定义成函数，登录成功直接调用主界面
def main_GUI():
    # 创建窗口
    root = Tk()
    # 修改窗口名字
    root.title('B测文件传输系统')
    # 修改窗口大小尺寸和位置
    root.geometry('600x400+200+100')
    # 创建标题标签
    lable = Label(root, text='B测文件传输系统', font=('Arial', 12), width=15, height=2)
    lable.pack()

    '''
    # 创建输入框，并修改宽度参数
    ent = Entry(root, width=50)
    # 布局控件(显示输入框)
    ent.pack()
    '''

    def upload():
        file_path = filedialog.askopenfilename(title='选择文件')  # 选择文件返回文件名
        file_path = str(file_path)
        file_path = eval(repr(file_path).replace(r'/', r'\\'))  # filename是得到的文件的绝对路径
        # print(file_path)
        file_size = str(get_Filesize(file_path))
        file_size = file_size + 'M'
        # print(file_size + 'M')
        file_modify_time = get_FileModifyTime(file_path)
        file_name = os.path.split(file_path)
        # print(file_name[1])
        # Client_def.Client(filename)  # 先是import的文件名，然后是其中的函数名
        pymysql_.insert(file_path, file_name[1], file_modify_time, file_size)  # 这里file_name是一个元组，其中第二个元素才是文件名
        Client_.Client(file_path)
        messagebox.showinfo('Successful', '文件已成功上传!')

    # 获取文件的大小,单位是M
    def get_Filesize(filePath):
        # filePath = filePath.unicode(filePath,'utf8')
        file_size = os.path.getsize(filePath)
        file_size = file_size / float(1024 * 1024)
        return round(file_size, 2)

    # 时间戳转换为时间
    def TimeStampToTime(timestamp):
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

    # 获取文件最后修改时间
    def get_FileModifyTime(filePath):
        # filePath = filePath.unicode(filePath,'utf8')
        t = os.path.getmtime(filePath)
        return TimeStampToTime(t)

    # 根据用户输入ID，下载对应的文件
    def download():
        # 获取到用户的输入下载文件所对应的id
        input_id = entry_id.get()
        print(input_id)
        file_path = pymysql_.select_name(input_id)
        print(file_path)
        file_path = r'C:\\Users\\lx223\\Desktop\\Python\\Python_test\\static\\' + file_path
        print(file_path)
        Client_def.Client(file_path)
        messagebox.showinfo('Successful', '文件已成功下载!')

    # 定义函数，调用disk_size.py返回并显示当前磁盘剩余空间,并显示出
    def return_disk_size():

        size = disk_size.get_free_space_mb('C:\\Users\\lx223\\Desktop\\Python\\B_test')
        #print(size)
        size = str(round(size,2))+'G'
        size = '当前磁盘剩余量:'+ size
        messagebox.showinfo('当前磁盘剩余量，单位G',size)
        upload()

    # 定义函数，清空输入框中的内容
    def refresh():
        root.destroy()  # 关闭当前窗口
        main_GUI()  # 打开新的主窗口

    # 定义主界面的表格，显示文件的信息栏
    columns = ("ID", "文件名称", '最后修改时间', '文件大小')
    treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

    treeview.column("ID", width=50, anchor='center')  # 表示列,不显示
    treeview.column("文件名称", width=100, anchor='center')
    treeview.column("最后修改时间", width=150, anchor='center')
    treeview.column("文件大小", width=60, anchor='center')

    treeview.heading("ID", text="ID")  # 显示表头
    treeview.heading("文件名称", text="文件名称")
    treeview.heading("最后修改时间", text="最后修改时间")
    treeview.heading("文件大小", text="文件大小")

    treeview.pack(side=LEFT, fill=BOTH)

    # 定义4个空列表存储文件的信息，并接受 pymysql_ 中的file_con()函数返回的文件信息
    row_ID = []
    row_name = []
    row_time = []
    row_size = []
    (row_ID, row_name, row_time, row_size) = pymysql_.file_con(row_ID, row_name, row_time, row_size)

    # 将接受到的文件信息写入界面的表格中
    for i in range(min(len(row_ID), len(row_name), len(row_time), len(row_size))):  # 写入数据
        treeview.insert('', i, values=(row_ID[i], row_name[i], row_time[i], row_size[i]))

    # 创建下载ID输入文本框
    # 创建输入框标签
    label_id = Label(root, text='下载ID:', justify=RIGHT, width=100)
    # 将标签放到窗口上
    label_id.place(x=370, y=150, width=100, height=20)
    # 创建文本框，同时设置关联的变量
    input_id = StringVar()
    input_id.set('')
    entry_id = Entry(root, width=100, textvariable=input_id)
    entry_id.place(x=400, y=180, width=100, height=20)

    # 创建upload Button并显示,调用上传功能的upload()函数
    btn_upload = Button(root, text='  Upload   ', command=return_disk_size)
    # btn_upload.place(x=380,y=50)
    btn_upload.pack()

    # 创建download Button并显示，调用下载功能download()函数
    btn_download = Button(root, text='Download', command=download)
    # btn_download.place(x=380,y=150,anchor = NE)
    btn_download.pack()

    # 创建Refresh Button并刷新页面(关闭后再打开)
    btn_copy = Button(root, text=' Refresh ', command=refresh)
    # btn_copy.place(x=380,y=250)
    btn_copy.pack()

    # 显示窗口
    mainloop()



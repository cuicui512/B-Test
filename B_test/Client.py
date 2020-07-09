# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: Client.py
 @function: socket通信客户端
 @author:  linxin
 @date:  7/4/2020 - 10:56 AM
'''

import socket
import  tqdm
import os

#传输数据分隔符
SEPARATOR = "<SEPARATOR>"

#服务器信息
host = "192.168.10.1"  #主机
port = 5001     #端口号

#文件传输的缓冲区
BUFFER_SIZE = 4096

#传输的文件名字
filename = "C:\\Users\\lx223\\Desktop\\新建压缩(zipped)文件夹.zip"
#文件大小
file_size = os.path.getsize(filename)

#创建socket连接
s = socket.socket()
#连接服务器
print(f"服务器连接中{host}:{port}")
s.connect((host,port))
print("服务器连接成功！")

#发送文件名字和文件大小，必须进行编码处理encode()
s.send(f"{filename}{SEPARATOR}{file_size}".encode())
#文件传输
progress = tqdm.tqdm(range(file_size),f"发送{filename}",unit="B",unit_divisor=1024)  #progress是进度条
with open(filename,"rb") as f:
    for _ in progress:
        #读取文件
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        #sendall确保即使网络忙碌的时候数据任然可以传输
        s.sendall(bytes_read)
        progress.update(len(bytes_read))    #更新进度条
print(f"发送{filename}成功！")
#关闭资源
#s.close()
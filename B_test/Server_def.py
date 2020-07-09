# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: Server_def.py
 @function: 端口5002，对应下载时的客户端Client_def.py，定义成函数，Server_GUI可以调用函数并直接启动服务端
 @author:  linxin
 @date:  7/6/2020 - 11:12 PM
'''

import socket
import tqdm
import  os


# 设置服务器的IP和端口
SERVER_HOST = "192.168.10.1"
SERVER_PORT = 5002

# 设置文件读写的缓冲区
BUFFER_SIZE = 4096

# 传输数据分隔符
SEPARATOR = "<SEPARATOR>"

# 创建的Server
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))  # 服务器绑定端口
# 设置监听数
s.listen(5)
print(f"服务器监听{SERVER_HOST}:{SERVER_PORT}")
# 接受客户端连接
client_socket, address = s.accept()  # 接收后返回那一个客户 的socket，他的ip地址是多少
# 打印客户端的IP
print(f"客户端{address}连接")
# 接受客户端信息
received = client_socket.recv(BUFFER_SIZE).decode()
filename, file_size = received.split(SEPARATOR)  # 分割
# 获取文件的名字，不要路径
filename = os.path.basename(filename)  # 去除路径的影响，直接获取名字
file_size = int(file_size)  # file_size转为int类型

# 文件接收处理
progress = tqdm.tqdm(range(file_size), f"接受{filename}", unit="B", unit_divisor=1024, unit_scale=True)
# 开始写
with open(r'static_download/%s' % filename, "wb") as f:  # 写在本地的static目录下
    for _ in progress:
        # 从客户端读取数据
        bytes_read = client_socket.recv(BUFFER_SIZE)
        # 如果没有传输数据
        if not bytes_read:
            break
        # 读取写入
        f.write(bytes_read)
        # 更新进度条
        progress.update(len(bytes_read))

print(f"接受{filename}成功！")
# 关闭资源
# client_socket.close()       # 先关闭客户端
# s.close()   # 后关闭socket


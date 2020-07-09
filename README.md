# 西电B测——文件传输系统
2020.07

### 关于目前文件传输系统有的问题


1. 没有自定义的socket,直接用的python的socket进行传输

2. 下载的时候调用的客户/服务端和上传的时候的不一样(可以考虑将server/client都写成函数，端口号作为参数)

3. server端接受一次就会自动关闭，运行的时候现将两个服务端启动

4. 上传的文件在项目目录下的static文件，下载的文件放在子目录下的static_download文件夹下

5. 换了运行环境之后，对应的文件路径需要改成对应的主机或者服务器的路径


### 使用说明
1. 测试环境：python3  mysql5.7  win10
2. 将需要的包安装上
3. 建立数据库并修改链接文件中的数据库属性，数据库已导出，使用前记得把数据库清空
4. test.py是我用来测试bug的，登录界面从loginGUI开始运行，唯一用户名：admin,密码：123456
5. 使用前先将两个服务端运行起来，Server.py/Server_def.py
5. 进入主界面后upload按钮，选择文件，并上传到static目录下，Refresh按钮点击刷新列表，输入对应的ID号点击download进行下载到static_download目录下，
6. 本产品不出现致命问题不接受改bug请求


### 文档说明
1. 服务端有两个Server.py和Server_def.py，分别是用于上传和下载时的传输接受端

2. 客户端有两个写成函数的Client_.py和Client_def.py,分别用于上传和下载的时候的客户端

3. pymysql_.py是自己写的关于数据库处理的一些函数，使用时import后直接调用对应函数

4. disk_size.py可以返回当前路径下磁盘的剩余量

5. download_GUI.py 也是写成一个函数的形式，在loginGUI.py登录成功之后调用，里面包含了使用时的界面，其中，upload按钮上传，上传之后点击Refresh按钮刷新出新的上传记录，输入对应的编号点击download按钮即可下载

6. loginGUI.py是登陆的GUI，用户名，密码与数据库中不匹配的时候会弹出提示





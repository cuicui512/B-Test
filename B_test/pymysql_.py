# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: pymysql_.py
 @function: 客户端下载的时候会涉及到从数据库读取文件显示在主界面，从数据库中获取到文件的路径，所以写一个类直接封装涉及到其中对数据库的操作
 @author:  linxin
 @date:  7/6/2020 - 2:55 PM
'''

import pymysql

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='B_test', password='123456', database='B_test', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
'''
# sql语句,增删改
#sql = 'select birthday from t_user'
sql = 'select id,path,name from file'
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql)
print('查询的结果有%s条数据'%count)
# 获取第一行
dateOne = cur.fetchone()
print(dateOne)
print(dateOne[2])
'''
# 定义插入数据函数，向数据库中写入上传的文件的id,name,path,modify_time,size等属性
def insert(file_path, file_name, file_modify_time, file_size):
    sql = 'insert into file(path,name,modify_time,size) values(%s,%s,%s,%s) '
    cur.execute(sql,(file_path, file_name, file_modify_time, file_size))
    #count = cur.execute(sql,(file_path, file_name, file_modify_time, file_size))
   # print('插入的结果有%s条数据' % count)


# 定义查找函数，根据id查找文件并返回文件的路径
def select(id):
    sql = 'select path from file where id= {}'.format(id)
    #cur.execute(sql)
    count = cur.execute(sql)
    # print('查询的结果有%s条数据' % count)
    # 获取第一行
    dateOne = cur.fetchone()
    return dateOne[0]  # 返回文件的路径

# 定义查找函数，根据id查找文件并返回文件的名称，用于下载的时候更换保存位置路径
def select_name(id):
    sql = 'select name from file where id= {}'.format(id)
    #cur.execute(sql)
    count = cur.execute(sql)
    # print('查询的结果有%s条数据' % count)
    # 获取第一行
    dateOne = cur.fetchone()
    return dateOne[0]  # 返回文件的路径


# 定义函数，返回所有的文件信息，并重组后按列返回对应的元组
def file_con(row_ID, row_name, row_time, row_size):
    sql = 'select * from file'
    count = cur.execute(sql)
    result = cur.fetchall()
    result = list(result)  # 元组转换成列表
    row_ID, row_path, row_name, row_time ,row_size= [list(i) for i in zip(*result)]
    return row_ID, row_name, row_time, row_size

# 定义函数，参数为用户ID，查询数据库，返回验用户的密码
def password(user_id):
    # print(user_id)
    # print(type(user_id))
    sql = 'select password from user_ where  user_id= "%s" '% user_id   # 这里的%s必须是双引号，单引号不行的
    count = cur.execute(sql)
    dateOne = cur.fetchone()
    if dateOne:
        return dateOne[0]  # 返回用户对应的密码
    else:
        return 0
'''
sql = 'select path from file where value(%s) '
count = cur.execute(sql,'1')
print('查询的结果有%s条数据'%count)
'''


# 关闭
#cur.close()
#conn.close()
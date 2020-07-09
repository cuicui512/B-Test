# -*- coding: utf-8 -*-
'''
 @project: Python_test
 @file: disk_size.py
 @function: 返回当前文件夹所在磁盘剩余空间
 @author:  linxin
 @date:  7/7/2020 - 10:03 PM
'''

import ctypes
import os
import platform
import sys

# 定义函数，返回当前文件夹所在磁盘剩余空间
def get_free_space_mb(folder):
    """ Return folder/drive free space (in bytes)
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value/1024/1024/1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize/1024/1024/1024.


import ctypes
import os
import platform
import sys

# 定义函数，返货当前文件夹所在磁盘剩余空间
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

print(get_free_space_mb('C:\\Users\\lx223\\Desktop\\Python\\B_test'))
# -*- coding: utf-8 -*-

import os

def visitDir(path):
    if not os.path.isdir(path):
        print('Error:', path, ' is not a directory or does not exit.')
        return
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        print(sub_path)
        if os.path.isdir(sub_path):
            visitDir(sub_path)
            

def visitDir2(path):
    if not os.path.isdir(path):
        print('Error:', path, ' is not a directory or does not exit.')
        return
    list_dirs = os.walk(path)
    # 遍历该元组的目录 和 文件信息
    for root, dirs, files in list_dirs:   #  遍历 该元组的目录 和 文件信息
        for d in dirs:
            print(os.path.join(root, d))  # 获取 完整路径
        for f in files:
            print(os.path.join(root, f))  # 获取文件绝对路径
       
        
#visitDir('./')

visitDir2('./')


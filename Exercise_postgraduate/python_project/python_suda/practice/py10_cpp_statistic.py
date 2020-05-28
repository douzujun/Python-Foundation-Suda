# -*- coding: utf-8 -*-

from os.path import isdir, join
from os import listdir

AllLines = []           # 保存所有代码行
NotRepeatedLines = []   # 保存非重复的代码行

file_num = 0      # 文件数量
code_num = 0      # 代码总行数

def LinesCount(directory):
    global AllLines
    global NotRepeatedLines
    global file_num
    global code_num
    
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):                # 递归遍历子文件夹
            LinesCount(temp)
        elif temp.endswith('.cpp'):    #  只考虑.cpp文件
            file_num += 1
            # 打开目录下文件
            with open(temp, 'r') as fp:
                while True:
                    line = fp.readline()
                    if not line:
                        break
                    if line not in NotRepeatedLines:
                        NotRepeatedLines.append(line)  # 记录非重复行
                    code_num += 1                      # 记录所有代码行
    
    return (code_num, len(NotRepeatedLines))

path = 'G:/Dev-Cpp/代码大全/Offer'
print('代码总数量: {0[0]}, 非重复代码行数: {0[1]}'.format(LinesCount(path)) )
print('文件数量: {0}'.format(file_num))







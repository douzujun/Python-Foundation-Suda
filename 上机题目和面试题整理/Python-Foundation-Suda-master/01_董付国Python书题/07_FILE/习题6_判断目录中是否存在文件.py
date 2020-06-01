"""
用户输入目录和文件名，判断目录及其子目录中是否存在该文件。
"""

import os
os.chdir('../')
targetpath = input('请输入路径名')
filename = input('请输入文件名：')

for tup in os.walk(targetpath):
    # tup 路径名 路径下的目录列表 路径下的文件列表
    if filename in tup[2]:
        print("文件存在于",tup[0],"路径下。")
        break
else:
    print(filename, "下不存在此文件")
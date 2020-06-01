# 一个用来测试文件及目录操作的程序

# 文件的开启和关闭
fileObj = open("document_1.txt", 'r+')
words = fileObj.readline()
print(words, end="")
fileObj.close()

# 用 with 语句来自动调用 close() 方法
with open("document_1.txt", 'r+') as f:
    print("file \"document_1.txt\" has been opened! Sent by with open() as ")


# 避免文件打开异常
try:                            # 捕获异常法
    fileObj = open("document_2.txt", "r")
except FileNotFoundError:
    print('file "document_2.txt" not exisit! Sent by try except ')

import os                       # os模块判断文件是否存在
if not os.path.exists("document_2.txt"):
    print('file "document_2.txt" not exisit! Sent by os\n')

# 读文件的相关函数
fileObj = open("document_1.txt", 'r+')
words = fileObj.readline()      # 读取一行存到words
print(words,end="")

# words = fileObj.read(4)         # 读取N个字符
# print(words,end="")

line_list = fileObj.readlines() # 读取所有行并存到列表中
for L in line_list:
    print(L,end="")
fileObj.close()

# 利用for循环获取文件中的每一行
# for line in input():
#     print(line,end="")    #input 内输入的内容看做序列
for line in open("document_1.txt","r"):
    print(line,end="")

# 写文件相关函数
# output.write(str)
# output.writelines(seq)
output = open("document_3.txt", "w+")
output.write("'document_3.txt' has been writen\n")
output.writelines(line_list)
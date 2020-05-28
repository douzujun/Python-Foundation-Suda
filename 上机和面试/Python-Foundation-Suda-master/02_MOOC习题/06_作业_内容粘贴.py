"""
附件中有两个文件cat1.txt和cat2.txt，请编写程序将cat2的内容复制到cat1文件的最后面。
"""

floder = "./06_作业/"
file1_path = floder + "cat1.txt"
file2_path = floder + "cat2.txt"

file2 = open(file2_path, 'r')
content = file2.read()
file2.close()

file1 = open(file1_path, 'a')
file1.write(content)
file1.close()
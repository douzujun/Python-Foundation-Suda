"""
修改当前工作目录为C"\ 并验证，再修改回来
"""
import os

cwd = os.getcwd()
print("当前工作目录为：", cwd)
os.chdir("C:\\")
print("已经更改工作目录为：", os.getcwd())
os.chdir(cwd)
print("已将工作目录改回至：", os.getcwd())
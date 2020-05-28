"""
使用shutil中的move方法进行文件移动

"""
import shutil

print('e.g. GBK.txt, ./files')
src = input('请输入要移动的文件或目录：')
dst = input('请输入移动到的位置：')

shutil.move(src,dst)
# -*- coding: utf-8 -*-

# 用 IE 浏览器从 FTP 上下载 org.dat ，并保存在 D 盘的根目录下.
# 此文件中按文本方式存放了一段其他文章，其中有若干长度小于 15 的十进制或八进制数字，数字之间用 ,
# 分开，数字内部存在且仅存在空格.
# 八进制数以起始位 0 作为标示与十进制数区分.
#
# 顺序读取这些数字将他们转变为十进制数后按从大到小的顺序排序后，输出到 D 盘根目录下 new.txt ，每个
# 数字一行.
# eg ：  235 ,34  2, 043 1 ,1 3 ，分别是：十进制 235 ，十进制 342 ，八进制 431 ，十进制 13 ， _ 代表
#空格.
def int10(x):
    if x[0] == '0':
        return int(x, 8)
    return int(x)


def main():
    with open("./file/2009_org.dat", 'r+', encoding='utf8') as f:
        wds = f.read()
    
    # 按照","分割字符串
    words = wds.split(',')
    # 去除空格, 数字字符串转化成10进制整数
    words = [i.replace(" ","") for i in words]
    print(words)
    
    trans = list(map(int10, words))
    trans.sort(reverse=True)
    print(trans)
    
    with open('./file/2009_new.txt', 'w', encoding='utf8') as f:
        f.write(str(trans))
    
    
if __name__=='__main__':
    main()
# -*- coding: utf-8 -*-

# 2009. 
# 文件读取字符串，转数字【八进制/十进制】
# 此文件中按文本方式存放了一段其他文章，其中有 若干长度小于 15 的 十进制 或 八进制 数字，数字之间用 , 分开，
# 数字内部 存在且 仅存在 空格.
# 八进制数 以起始位 0 作为标示 与 十进制数区分.
# 顺序读取这些数字 将他们 转变为十进制数 后按 从大到小 的顺序排序后，
# 输出到文件，每个数字一行.
# eg ： 235,34_2,043_1_,1_3 ，分别是：十进制 235 ，十进制 342 ，八进制 431 ，十进制 13 ， _ 代表 空格.

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        wds = f.read()
    return wds

def int10(x):
    # 开头为 0，则为八进制
    if x[0] == '0':
        return int(x, 8)        # 将字符串数字，按8进制转换
    # 否则按10进制转换
    return int(x)

# 写文件
def writeFile(url, trans):
    with open(url, 'w', encoding='utf8') as f:
        f.write(str(trans))

def main():
    wds = readFile('./file/2009.txt')

    # 按照","分割字符串
    words = wds.split(',')
    
    # 去除空格，数字字符串转化成10进制整数
    words = [i.replace(" ", "") for i in words]
    print(words)
    
    trans = list(map(int10, words))
    print(trans)
    
    writeFile('./file/2009_out.txt', trans)
    
    
if __name__=='__main__':
    main()

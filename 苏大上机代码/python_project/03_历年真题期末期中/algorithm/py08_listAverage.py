# -*- coding: utf-8 -*-

import re

def sumAve(x):
    tmp = x
    cnt = 0
    res = 0
    while tmp:
        res += tmp%10
        tmp = int(tmp / 10)
        cnt = cnt + 1
    return res / cnt

def func8():
    num = input("输入字符串:")
    # 注意 [0-9]{3,5} 不要乱加空格，否则出错
    li = re.findall('[0-9]+', num)
    print(li)
    li = [int(elem) for elem in li if len(elem) >= 3 and len(elem) <= 5]
    print(li)
    
#    print(sumAve(2345))
    # 按照 数字和平均值 排序
    li.sort(key=lambda x:sumAve(x), reverse=True)
    print(li)

def main():
    func8()
    
if __name__=='__main__':
    main()

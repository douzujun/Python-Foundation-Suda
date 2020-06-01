# -*- coding: utf-8 -*-
import re

# 统计一个非空字符串中
# 1. 出现 次数最多的字符 及其 出现次数
# 2. 全部统计为大写字母
# 3. 结果 [字符, 对应次数]


def func7():
    s = input("输入一个字符串: ")
    # 字母转大写
    sli = list(s.upper())
    print(sli)
    
    # 统计列表元素的 频率
    sli = [(i, sli.count(i)) for i in sli]
    
    # 去重后，排序，返回列表
    sort_sli = sorted(set(sli), key=lambda x:-x[1])
    sort_sli = [list(i) for i in sort_sli]
    
    print("\n排序后去重的列表: ", sort_sli)
    
    print("\n次数最多: ", sort_sli[0])
    
    # 转换成字典: {'A': 5, 'D': 2, '1': 1, 'B': 1, 'G': 1}
    print(dict(sort_sli))


def main():
    func7()
    
    
if __name__=='__main__':
    main()





#-*- coding: utf8 -*-

import re
# 仅包含 小写字母 的两个单词 S 和 T 的 Jaccard系数（记为J）由如下三个统计量来确定：
# a：在两个单词中，都出现的字母的个数
# b：在S中出现，但没有在T中出现的字母的个数     len(S) - a
# c：在T中出现，但没有在S中出现的字母的个数     len(T) - a
# 那么J = a / (a + b + c)。给定两个单词S和T  
# 求确定其Jaccard系数的三个统计量a, b, c。


def fun6():
    S = input("输入单词S: ")
    T = input("输入单词T: ")
    # 分离字符 以及 生成集合[按字典序排序]
    sli = re.findall('[a-z]', S)
    slist = list(set(sli))
    tli = re.findall('[a-z]', T)
    tlist = list(set(tli))
    
    a = 0
    for i in range(0, len(slist)):
        for j in range(i, len(tlist)):
            if slist[i] == tlist[j]:
                a = a + 1
    
    b = len(slist) - a
    c = len(tlist) - a
    
    print((a, b, c))


def main():
    fun6()


if __name__ == '__main__':
    main()
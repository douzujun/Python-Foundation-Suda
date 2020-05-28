# -*- coding: utf-8 -*-

# 2005.2 统计篇文章中 各英文字母 的个数，并排序
import re

# 读取文章 各英文字母 如: 'test' --> ['t','e', 's','t']
def words(text):
    return re.findall('[a-z]', text.lower())


# 统计各英文字母的 个数
def train(features):
    # 存放结果
    model = {}
    for f in features:
        # 如果 f单词未出现过，默认值为0;
        # 否则，次数 + 1
        model[f] = model.get(f, 0) + 1
        
    return model


def main():
    statistic = train(words(open('./file/2005.txt').read()))
    
    # 对统计结果进行排序： 个数降序排列， 个数相同则按字母序排序
    statistic = sorted(statistic.items(), key=lambda x:(x[1], x[0]), reverse=True)
    print(statistic)
    
    
if __name__=='__main__':
    main()
# -*- coding: utf-8 -*-

# 2008.
# 此文件中按文本方式存放了一段其他文章，其中有若干长度小于 15 的英文单词，单词之间用空格分开，无其他符号.
# 顺序读取这段文章的不同的单词(大小写敏感)，同时在读取的过程中排除所有的单词 THE 以及变形，即这些单词不能出现在读取的结果中.
# 将读取的所有单词的首字母转大写后，输出 到文件 ，每个单词一行.

import re

# 读取所有字符串
# 匹配单词
def words(text : str):
    return re.findall('[a-zA-Z]+', text)

# 读文件
# 筛选单词
def train():
    with open('./file/2008.dat', 'r', encoding='utf8') as f:
        wds = f.read()
        
    wds = words(wds)
    print(wds)
    
    # 筛选 除了 the 的单词
    wds = [i.capitalize() for i in wds if i.lower() != 'the']
    print('\n', wds)
    
    with open('./file/2008_out.txt', 'w', encoding='utf8') as f:
        for word in wds:
            f.write(word + '\n')
      
        
train()


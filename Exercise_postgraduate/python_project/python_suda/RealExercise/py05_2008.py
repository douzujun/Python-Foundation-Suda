# -*- coding: utf-8 -*-

# 用 IE 从 FTP 上下载 org.dat ，并保存在 D 盘的根目录中.
# 此文件中按文本方式存放了一段其他文章，其中有若干长度小于 15 的英文单词，
# 单词之间用空格分开，无其他符号.

# 顺序读取这段文章的不同的单词(大小写敏感)，同时在读取的过程中排除所有的单词 THE 以及变形，
# 即这些单词不能出现在读取的结果中.

# 将读取的所有单词的首字母转大写后，输出 D 根目录下 new.txt ，每个单词一行.
import re

def words(text : str):
    return re.findall('[a-zA-Z]+', text)
#    return text.split()                  # 只匹配字符串


def train():
    with open("./file/2008.dat", 'r', encoding='utf8') as f:
        wds = f.read()
        
    wds = words(wds)
    print(wds)
    
    wds = [i.capitalize() for i in wds if i.lower() != "the"]
    print("\n", wds)
    
    with open("./file/2008_new.txt", 'w', encoding='utf8') as f:
        for word in wds:
            f.write(word+'\n')
    
    
        
train()
    
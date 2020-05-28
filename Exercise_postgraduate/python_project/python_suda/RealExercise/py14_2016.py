# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:44:08 2020

@author: douzi
"""

# 文本文件 input.txt 由若干英文单词和分隔符(空格，回车，换行)构成. 
# 根据如下说明编写程序：
# 统计不同单词出现的次数(频度). 
# 将统计结果按出现频度从高到低排序，并将出现频度大于 5 的单词及其频度输出到文件 output.txt
# 中. 文件格式如图所示
# 多个连续的分隔符被视为一个分隔符.
# 大小写敏感.
# 每个单词的长度不超过 20 个字符.
# 单词的数量未知. 如使用定义静态大数组的方式来统计，将被扣除 5 分.
import re

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
    return data

def train(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    return freq

def writeFile(sorted_freq):
    with open('./file/file_2016_output.txt', 'w', encoding='utf8') as f:
        for elem in sorted_freq:
            if elem[1] > 5:
                f.write("{0}, {1}\n".format(elem[0], elem[1]))
    

def main():
    data = readFile('./file/file_2016_in.txt')
    words = re.findall('[a-zA-Z]+', data)
    print(words)
    
    freq = train(words)
    sorted_freq = sorted(freq.items(), key=lambda x:(x[1]), reverse=True)
    print("\n", sorted_freq, "\n")
    for elem in sorted_freq:
        if elem[1] > 5:
            print("{0}, {1}".format(elem[0], elem[1]))
            
    writeFile(sorted_freq)


if __name__=='__main__':
    main()    
    













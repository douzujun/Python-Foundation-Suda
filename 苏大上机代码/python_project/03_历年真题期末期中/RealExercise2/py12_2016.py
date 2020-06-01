# -*- coding: utf-8 -*-

# 文本文件 input.txt 由若干英文单词和分隔符(空格，回车，换行)构成. 
# 统计不同单词出现的次数(频度). 
# 将统计结果按出现频度从高到低排序，并将出现频度大于 5 的单词 及 其频度 输出到文件 output.txt
# 中. 文件格式如图所示
# 1. 多个连续的分隔符被视为一个分隔符.
# 2. 大小写敏感.
# 3. 每个单词的长度不超过 20 个字符.
import re

# 读文件
def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
    return data

# 统计单词频度
def train(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    return freq

# 写文件
def writeFile(url, sorted_freq):
    with open(url, 'w', encoding='utf8') as f:
        for elem in sorted_freq:
            if elem[1] > 5:
                f.write("{0}, {1}\n".format(elem[0], elem[1]))
            else:
                break


def main():
    data = readFile('./file/file_2016_in.txt')
    words = re.findall('[a-zA-Z]+', data)
#    print(words)
    
    freq = train(words)
    sorted_freq = sorted(freq.items(), key=lambda x:(x[1]), reverse=True)
#    print(sorted_freq)
    for elem in sorted_freq:
        if elem[1] > 5:
            print('{0}, {1}'.format(elem[0], elem[1]))
    
    # 写文件
    writeFile("./file/file_2016_out.txt", sorted_freq)
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

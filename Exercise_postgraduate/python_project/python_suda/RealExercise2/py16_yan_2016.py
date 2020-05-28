# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:09:00 2020

@author: douzi
"""

# 2016保研题目
def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        data = data.split('\n')
        return data
    
# 用 words 里的单词 匹配sentence
def splitEssay(sentence, words):
    start, length = 0, len(sentence)
    res = []
    while start <= length:
        for k in range(20, 0, -1):          # k 是步长, 所以从最大单词长度开始匹配
            if sentence[start:start + k] in words: 
                res.append(sentence[start : start + k])
                break 
        start += k        # 从下一个地方【步长为k】开始匹配
            
    return " ".join(res)

    
def main():
    # input.txt 中存储了一个「丢失」了空格和标点符号的英文文章
    sentences = readFile('./file/file_2016yan_input.txt')
    # words.txt 中存储了不超过 30000 条的英文单词，每个单词占一行
    words = readFile('./file/file_2016yan_word.txt')
    print(sentences)
    print(words)
    
    # 将 data 用word分割 
    for sentence in sentences:
        # 用 words里的单词 匹配sentence
        # 如果 sentence里单词在words出现，则组成一个句子 
        essay = splitEssay(sentence, words)
        print(essay)
        

if __name__=='__main__':
    main()



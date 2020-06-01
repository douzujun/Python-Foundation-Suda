# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:14:09 2020

@author: douzi
"""

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        txt = data.split('\n')
    
    return txt

def splitEssay(sentence, words):
    
    start, sen_len = 0, len(sentence)
    res = []
    while start < sen_len:
        for k in range(20, 0, -1):
            # 长度为 k 
            if sentence[start:start+k] in words:
                res.append(sentence[start:start+k])
                break
        start += k        # 更新位置
    return res

def main():
    words = readFile('./file/file_2016_word.txt')
    print("词典: ", words, "\n")
    essay = readFile('./file/file_2016_input.txt')
    print("无空格文章: ", essay, "\n")
    
    for word in words[-3:]:
        print(word)
        
    # 显示文章的第一行 和 最后一行
    first = splitEssay(essay[0], words)
    last = splitEssay(essay[-1], words)
    
    print("\n文章第一行: {0}\n".format(' '.join(first)))
    
    print("文章最后一行: {0}\n".format(' '.join(last)))
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:32:31 2020

@author: douzi
"""
import re

def readWordsFromFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
    # 读取所有单词
    return re.findall('[a-zA-Z]+', data)

# wordlst中存在 某个字母 至少出现num次的单词
def findMultiAlphaWords(wordlst, num):
    wordResultLst = []
    for word in wordlst:
        w = list(word.lower())
        for e in w:
            if w.count(e) >= num:
                wordResultLst.append(word)
                break
    return wordResultLst

# ----删除wordResultLst中重复单词的多余份数，只保留一份-----
def delMultiData(wordResultLst):
    wset = list(set(wordResultLst))
    wordResultLst.clear()
    for elem in wset:
        wordResultLst.append(elem)


# 输出所有单词，每行输出4个单词，要求每个单词占20列
def printWordLst(wordResultLst, count):
    wlen = len(wordResultLst)
    for i in range(0, wlen):
        print("{0:20}".format(wordResultLst[i]), end='')
        if (i+1) % count == 0:
            print('')
    print('')
        
# word -> sum(ascii)
def ASCII(word):
    res = 0
    w = list(word)
    for e in w:
        res += ord(e)
    return res

# 将wordResultLst中的每一个单词转换成一个整数，保存到列表numLst中
def getNumberOfWords(wordResultLst):
    return [ASCII(word) for word in wordResultLst]
    
# 所有整数按整数的数字累加和
def numSum(num):
    res = 0
    num = list(str(num))
    for e in num:
        res += int(e)
    return res
    
# ----对numlst中的所有整数进行根据数字累加和进行降序排序----
def sortByDigitalSum(numlst : list):
    numlst.sort(key=lambda x:numSum(x), reverse=True)
    return numlst

 #输出整数列表，每行输出5个整数 
def printNumLst(numlst, count):
    nlen = len(numlst)
    for i in range(0, nlen):
        print("{0:8}".format(numlst[i]), end='')
        if (i+1) % count == 0:
            print('')
    print('')
    
# ----统计数字出现的次数----------
def staticDigitalTimes(numlst):
    resultDic = {}
    for e in numlst:
        num = str(e)
        for w in num:
            resultDic[w] = resultDic.get(w, 0) + 1
    return resultDic
    

# ===出现次数最多的数字===
def printDicToFile(url, resultDic):
    with open(url, 'w', encoding='utf8') as f:
        res = sorted(resultDic.items(), key=lambda x:(x[1]), reverse=True)
        print("{0:<2}:{1:>3}".format(res[0][0], res[0][1]))
        f.write("{0:<2}:{1:>3}".format(res[0][0], res[0][1]))
    

if __name__ == "__main__":   
    # ----从data.txt文件中读取所有单词-------
    wordlst = readWordsFromFile("./file/file_midterm2017.txt")
    print("文件中单词个数:", len(wordlst))  # 输出单词个数

    # ----找出单词中，存在某个字母重复num次的单词-----
    wordResultLst = findMultiAlphaWords(wordlst, 2)
    print("至少含有重复2次的字母的单词：", len(wordResultLst))

    # ----删除wordResultLst中重复单词的多余份数，只保留一份-----
    delMultiData(wordResultLst)
    print("===删除重复单词的多余单词后的结果===")
    printWordLst(wordResultLst, 4)  # 输出所有单词，每行输出4个单词
    
    # ----将wordResultLst中的所有单词转换为整数------
    numlst = getNumberOfWords(wordResultLst)

    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    sortByDigitalSum(numlst)
    print("===整数降序排序的结果===")
    printNumLst(numlst, 5)          # 输出整数列表，每行输出5个整数 
    
    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    
    print("===出现次数最多的数字===")
    printDicToFile("./file/file_midterm2017_out.txt", resultDic)




























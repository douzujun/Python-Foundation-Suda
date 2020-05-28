# -*- coding: utf-8 -*-

import re

def readWordsFromFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        words = re.findall('[a-zA-Z]+', data)
    return words

def findMultiAlphaWords(wordlst, cnt):
    wordResultLst = []
    for word in wordlst:
        w = list(word.lower())
        for e in w:
            if w.count(e) >= cnt:
                wordResultLst.append(word)
                break
    print(wordResultLst)
    return wordResultLst

def delMultiData(wordResultLst):
    tmp = wordResultLst[::]
    for elem in tmp:
        if wordResultLst.count(elem) > 1:
            wordResultLst.remove(elem)
    
def printWordLst(wordResultLst, cnt):
    wlen = len(wordResultLst)
    for i in range(0, wlen):
        print('{0:20}'.format(wordResultLst[i]), end='')
        if (i + 1) % cnt == 0:
            print('')
    print('')
    
def ASCII(word):
    ans = 0
    for w in word:
        ans += ord(w)
    return ans
    
def getNumberOfWords(wordResultLst):
    numlst = []
    for word in wordResultLst:
        numlst.append(ASCII(word))
    return numlst

def numSum(x):
    li = str(x)
    res = 0
    for e in li:
        res += int(e)
    return res

def sortByDigitalSum(numlst):
    numlst.sort(key=lambda x:numSum(x), reverse=True)
    return numlst        

def printNumLst(numlst, cnt):
    wlen = len(numlst)
    for i in range(0, wlen):
        print('{0:8}'.format(numlst[i]), end='')
        if (i + 1) % cnt == 0:
            print('')
    print('')

# ----统计数字出现的次数----------
def staticDigitalTimes(numlst):
    resultDic = {}
    for e in numlst:
        num = str(e)
        for w in num:
            resultDic[w] = resultDic.get(w, 0) + 1
    print(resultDic)
    return resultDic
    
def printDicToFile(url, resultDic):
    resultDic = sorted(resultDic.items(), key=lambda x:x[1], reverse=True)
    with open(url, 'w', encoding='utf8') as f:
        print('{0:<2}:{1:>3}'.format(resultDic[0][0], resultDic[0][1]))
        f.write('{0:<2}:{1:>3}'.format(resultDic[0][0], resultDic[0][1]))

if __name__ == "__main__":   
    # ----从data.txt文件中读取所有单词-------
    wordlst = readWordsFromFile("./file/file_midterm_2017.txt")
    print("文件中单词个数:", len(wordlst))  # 输出单词个数
    # ----找出单词中，存在某个字母重复num次的单词-----
    wordResultLst = findMultiAlphaWords(wordlst, 2)
    print("至少含有重复2次的字母的单词：", len(wordResultLst))
#​
    # ----删除wordResultLst中重复单词的多余份数，只保留一份-----
    delMultiData(wordResultLst)
    print("===删除重复单词的多余单词后的结果===")
    printWordLst(wordResultLst, 4)  # 输出所有单词，每行输出4个单词
    
    # ----将wordResultLst中的所有单词转换为整数------
    numlst = getNumberOfWords(wordResultLst)
    
    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    sortByDigitalSum(numlst)
    print("===整数降序排序的结果===")
    printNumLst(numlst, 5)    #输出整数列表，每行输出5个整数 
    
    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    
    print("===出现次数最多的数字===")
    printDicToFile("./file/file_midterm_2017.out", resultDic)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-

import re

# 编写一个函数，从data.txt文件中读取所有单词，并保存到单词列表wordlst中。
def readWordsFromFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        words = re.findall('[a-zA-Z]+', data)
        print(words)
    return words

#编写一个函数，找出wordlst中存在某个字母 至少出现num次 的单词，字母不区分大小写，
#将符合要求的单词保存到列表 wordResultLst 中，其中num由参数给出
def findMultiAlphaWords(wordlst, num):
    wordResultLst = []
    for word in wordlst:
        w = list(word.lower())   # 注意：不区分大小写
        for e in w:
            if w.count(e) >= num:
                wordResultLst.append(word)
                break
    print(wordResultLst)
    return wordResultLst

# ----删除wordResultLst中重复单词的多余份数，只保留一份-----
def delMultiData(wordResultLst):
    tmp = wordResultLst[::-1]
    for elem in tmp:
        if wordResultLst.count(elem) > 1:
            wordResultLst.remove(elem)

# 输出所有单词，每行输出4个单词
def printWordLst(wordResultLst, num):
    wlen = len(wordResultLst)
    for i in range(0, wlen):
        print("{0:20}".format(wordResultLst[i]), end='')
        if (i+1) % num == 0:
            print('')
    print('')
    
# word --> sum(ascii)
def ASCII(word):
    res = 0
    w = list(word)
    for e in w:
        res += ord(e)
    return res
    
# ----将wordResultLst中的所有单词转换为整数------
def getNumberOfWords(wordResultLst):
    return [ASCII(word) for word in wordResultLst]

def numSum(num):
    li = str(num)
    res = 0
    for e in li:
        res += int(e)
    return res

# ----对numlst中的所有整数进行根据数字累加和进行降序排序----
def sortByDigitalSum(numlst):
    numlst.sort(key=lambda x:numSum(x),reverse=True)
    return numlst

#输出整数列表，每行输出5个整数 
def printNumLst(numlst, num):
    wlen = len(numlst)
    for i in range(0, wlen):
        print("{0:8}".format(numlst[i]), end='')
        if (i+1) % num == 0:
            print('')
    print('')

# ----统计数字出现的次数----------
def staticDigitalTimes(numlst):
    resultDic = {}
    for e in numlst:
        num = str(e)
        for w in num:
            # 默认为0，否则次数+1
            resultDic[w] = resultDic.get(w, 0) + 1
    return resultDic

# ===出现次数最多的数字===
# 数字(占2列,左对齐) ：出现次数(占3列，右对齐)
def printDicToFile(url, resultDic):
    with open(url, 'w', encoding='utf8') as f:
        res = sorted(resultDic.items(), key=lambda x:(x[1]), reverse=True)
        print('{0:<2}:{1:>3}'.format(res[0][0], res[0][1]))
        f.write('{0:<2}:{1:>3}'.format(res[0][0], res[0][1]))

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
    printWordLst(wordResultLst, 4)  #输出所有单词，每行输出4个单词

    # ----将wordResultLst中的所有单词转换为整数------
    numlst = getNumberOfWords(wordResultLst)

    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    sortByDigitalSum(numlst)
    print("===整数降序排序的结果===")
    printNumLst(numlst, 5)    #输出整数列表，每行输出5个整数 

    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    print("===出现次数最多的数字===")
    printDicToFile("./file/file_midterm2017_out.txt", resultDic)
    
    
    
    
    
    
    
    
    
    
    
    
    
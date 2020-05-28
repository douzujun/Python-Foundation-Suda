def readWordsFromFile(filename):
    """
    1.	编写一个函数，从data.txt文件中读取所有单词，并保存到单词列表wordlst中。
    :param filename:
    :return: str
    """
    f = open(filename, 'r')
    file_str = ' '.join(f.readlines())
    f.close()
    # 翻译表 去掉字符串中的,.
    transtable = ''.maketrans(',.\n\t ', '     ')
    file_str = file_str.translate(transtable)
    return file_str.split()


def findMultiAlphaWords(wordlst, num):
    """
    找出wordlst中存在某个字母至少出现num次的单词，
    字母不区分大小写，将符合要求的单词保存到列表wordResultLst中，其中num由参数给出。
    """
    wordResultLst = []
    wordlst = list(map(lambda x: x.lower(), wordlst))
    for word in wordlst:
        for ch in word:
            if word.count(ch) == num:
                wordResultLst.append(word)
                break
    return wordResultLst


def delMultiData(wordResultLst):
    """
    3.	编写一个函数，删除wordResultLst中重复单词多余份数，只保留一份，
    非重复单词保持不变。将结果仍然保存在列表wordResultLst中。
    :param wordResultLst:
    :return:
    """
    temp = list(set(wordResultLst))
    wordResultLst.clear()
    wordResultLst.extend(temp)


def printWordLst(wordlst, count):
    """
    4.	编写一个函数，输出wordResultLst中所有单词，要求每个单词占20列，每行输出count个单词，其中count由参数给出。
    :param wordlst:
    :param row:
    :return:
    """
    i = 0
    for word in wordlst:
        print(word.ljust(20, ' '), end='')
        i += 1
        if i % count == 0:
            print('')
    if i%count !=0:
        print('')


def getNumberOfWords(wordlst):
    """5.	编写一个函数，将wordResultLst中的每一个单词转换成一个整数，保存到列表numLst中。
    转换规则：整数为单词的所有字母的ASCII值的累加和，例如：sum对应的整数就是s、u、m三个字母的ASCII值之和。
    """
    numlst = []
    for word in wordlst:
        s = 0
        for ch in word:
            s += ord(ch)
        numlst.append(s)
    return numlst


def sortByDigitalSum(numLst):
    """
    6.	编写一个函数，对numLst中的所有整数按整数的数字累加和进行降序排序，
    例如整数:923,456,134对应的整数数字累加和为14，15，8，则排序结果456，923，134。
    :return:
    """
    def countvalue(num):
        temp = 0
        while num != 0:
            temp += num % 10
            num //= 10
        return temp

    numLst.sort(key=lambda x:countvalue(x), reverse=True)
    # numLst.extend(sorted(zip(numLst, sumlist), key=lambda x: x[1], reverse=True))


def printNumLst(numLst, count):
    """7.	编写一个函数，输出排序后的numLst，要求每个整数占8列，每行输出count个整数，其中count由参数给出。"""
    i = 0
    for num in numLst:
        print(str(num).ljust(8, ' '), end='')
        i += 1
        if i % count == 0:
            print('')


def staticDigitalTimes(numlst):
    """统计numLst中每个数字出现的次数，将统计结果保存到字典resultDic中"""
    resultDic = dict()
    for num in numlst:
        while num!=0:
            temp = num%10
            resultDic[temp] = resultDic.get(temp, 0) + 1
            num //= 10
    return resultDic


def printDicToFile(filename, resultDic):
    f = open(filename, 'w')
    result_list = sorted(resultDic, key=lambda x: resultDic[x], reverse=True)
    maxvalue = max(resultDic.values())
    for num in result_list:
        if resultDic[num] == maxvalue:
            s = '{0:<2}:{1:>3}'.format(num, resultDic[num])
            print(s)
            f.write(s)
    f.close()


if __name__ == "__main__":
    # ----从data.txt文件中读取所有单词-------
    # wordlst = readWordsFromFile("d:\\data.txt")
    wordlst = readWordsFromFile(r"D:\CODE\PythonFoundation\Training\Suda\03_data.txt")
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
    printNumLst(numlst, 5)  # 输出整数列表，每行输出5个整数

    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    print("===出现次数最多的数字===")
    printDicToFile(r"D:\CODE\PythonFoundation\Training\Suda\03_result.txt", resultDic)

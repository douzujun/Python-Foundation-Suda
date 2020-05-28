#-*- coding: utf-8 -*-

import random

def productRndNum():
    random.seed(100)
    rnd = random.randint(100, 200)
    numberLst = [random.randint(100, 500) for i in range(rnd)]
    return numberLst

def getDigNumber(numberLst, digLst):
    num26Lst = []
    for num in numberLst:
        if str(digLst[0]) in str(num) or str(digLst[1]) in str(num):
            num26Lst.append(num)
    return num26Lst    

def printOut(num26Lst, num):
    nlen = len(num26Lst)
    for i in range(nlen):
        print('{0:>5}'.format(num26Lst[i]), end='')
        if (i + 1) % num == 0:
            print('')
    print('')

#-----找出所有整数的因子-----
def getDivisorNum(num26Lst):
    resultLst = []
    for num in num26Lst:
        for i in range(2, num):
            if num % i == 0:
                resultLst.append(i)
    return resultLst

# -----统计每个因子出现的次数-----
def staticResult(resultLst):
    freq = {}
    for num in resultLst:
        freq[num] = freq.get(num, 0) + 1
    return freq

def printMax5Out(resultStatic):
    resultStatic = sorted(resultStatic.items(), key=lambda x: x[1], reverse=True)
    for key, value in resultStatic[:5]:
        print(key, value)

def delMultiDivisor(resultLst):
    tmp = sorted(set(resultLst), key=resultLst.index)
    resultLst.clear()
    resultLst.extend(tmp)

def printDivisorToFile(url, resultLst):
    with open(url, 'w', encoding='utf8') as f:
        rlen = len(resultLst)
        for i in range(rlen):
            f.write('{0:>5}'.format(resultLst[i]))
            if (i + 1) % 8 == 0:
                f.write('\n')

if __name__ == "__main__":
    # ----产生随机整数-------
    numberLst = productRndNum()
    # ----找出包含数字2或6的整数，其中digLst包含数字2和6-----
    num26Lst = getDigNumber(numberLst, digLst=[2, 6])
    printOut(num26Lst, 8)
    #-----找出所有整数的因子-----
    resultLst = getDivisorNum(num26Lst)
    # -----统计每个因子出现的次数-----
    resultStatic = staticResult(resultLst)
    printMax5Out(resultStatic)
    # ----删除resultLst中重复因子的多余份数，只保留一份-----
    delMultiDivisor(resultLst)
    print("===出现次数最多的数字===")
    printDivisorToFile("./file/file_yan2018_result.txt", resultLst)
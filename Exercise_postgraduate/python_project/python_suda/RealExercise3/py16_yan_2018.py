# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import random
# 产生一个100-200之间的随机整数 rmd
# 再产生rmd个100至500以内的随机整数，保存到numberLst
def productRndNum():
    random.seed(100)
    rmd = random.randint(100, 200)  # [100,200]
    numberLst = [random.randint(100, 500) for i in range(rmd)]
    return numberLst

# ----找出包含数字2或6的整数，其中digLst包含数字2和6-----
def getDigNumber(numberLst, digLst):
    num26Lst = []
    for nb in numberLst:
        nstr = str(nb)
        for e in digLst:
            if str(e) in nstr:
                num26Lst.append(nb)
                break
    return num26Lst

# 每行输出8个整数，每个整数占5列，右对齐
def printOut(num26Lst, cnt):
    nlen = len(num26Lst)
    for i in range(nlen):
        print("{0:>5}".format(num26Lst[i]), end=' ')
        if (i + 1) % cnt == 0:
            print('')
    print('')

#-----找出所有整数的因子, 因子不包括1和整数本身-----
def getDivisorNum(num26Lst):
    resultLst = []
    for numb in num26Lst:
        t = numb
        i = 2
        while i < t:
            if t % i == 0:
                resultLst.append(i)
            i = i + 1
    return resultLst

# 统计resultLst中每个因子出现的次数
def staticResult(resultLst):
    freq = {}
    for num in resultLst:
        freq[num] = freq.get(num, 0) + 1
    return freq

def printMax5Out(resultStatic):
    resultStatic = sorted(resultStatic.items(), key=lambda x:(x[1]), reverse=True)
    for elem in resultStatic[:5]:
        print("{0} : {1}".format(elem[0], elem[1]))

def delMultiDivisor(resultLst):
    resultLst = sorted(set(resultLst), key=resultLst.index)
    return resultLst

# 将删除重复因子的resultLst列表输出到D盘文件result.txt中，
# 要求每行输出8个整数，每个整数占5列，右对齐
def printDivisorToFile(url, resultLst):
    with open(url, 'w', encoding='utf8') as f:
        rlen = len(resultLst)
        for i in range(rlen):
            f.write('{0:>5}'.format(resultLst[i]))
            if (i + 1) % 8 == 0:
                f.write('\n')
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
    
    
    
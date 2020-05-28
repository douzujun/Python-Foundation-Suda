# -*- coding: utf-8 -*-

# 2013. 图论问题-->转换成问题: 
# 两顶点间 存在长度为k的路径
# 1. PVG -> PEK
# 即：PVG -> CAN -> PEK
# PathInput.txt
# 6
# [PVG, CAN]
# [CAN, PEK]
# [PVG, CTU]
# [CTU, DLC]
# [DLC, HAK]
# [HAK, LXA]
# PathRequest.txt
# 2
# [PVG, DLC, 2]
# [PVG, LXA, 2]
# output:
# [PVG, DLC, YES]
# [PVG, LXA, NO]
import re

# 读文本文件内容，以换行分隔单词，返回字符串列表
def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        wds = f.readlines()
        return wds

# 两顶点间 存在长度为k的路径
# countLine: Line的长度
# 递归判断起点: start
# 终点为: end
# 长度为k的路径是否存在
def check(Line, countLine, start, end, k):
    flag = 0
    # 遍历所有 Line 的数据
    # [['PVG', 'CAN'], ['CAN', 'PEK'], ['PVG', 'CTU'], ['CTU', 'DLC'], ['DLC', 'HAK'], ['HAK', 'LXA']] 
    for i in range(countLine):
        # 如果找到路径
        if k == 0 and Line[i][0] == start and Line[i][1] == end:
            flag = 1     # 为真
            break
        elif k > 0 and Line[i][0] == start and Line[i][1] != end:
            k -= 1
            # 改变 起点 继续递归判断
            flag = check(Line, countLine, Line[i][1], end, k)
    
    return flag

# Line: Line的数据
# Path: Path的数据
def writeFile(url, Line, countLine, Path, countPath):
    with open(url, 'w', encoding='utf8') as f:
        # countPath操作次数
        for i in range(countPath):
            # 起点，终点，step=2
            # 两顶点间 存在 长度为k的路径 --> PVG-->DLC(路径2): YES
            if check(Line, countLine, Path[i][0], Path[i][1], Path[i][2]):
                f.write('[{0}, {1}, YES]\n'.format(Path[i][0], Path[i][1]))
            else:
                f.write('[{0}, {1}, No]\n'.format(Path[i][0], Path[i][1]))
    

def main():
    dataLine = readFile('./file/file_2013_PathInput.txt')
    dataPath = readFile('./file/file_2013_PathRequest.txt')
#    print(dataLine)
#    print(dataPath)
    # 路径数
    countLine, countPath = int(dataLine[0]), int(dataPath[0])
    
    Line, Path = [], []
    for i in range(1, countLine + 1):
        Line.append([dataLine[i][1:4], dataLine[i][6:9]])

    for i in range(1, countPath + 1):
        Path.append([dataPath[i][1:4], dataPath[i][6:9], int(dataPath[i][11])])

    # 输出 Line 的数据
    print(Line)
    print(Path)
    
    writeFile('./file/file_2013_output.txt', Line, countLine, Path, countPath)

    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
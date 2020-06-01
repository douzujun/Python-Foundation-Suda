# -*- coding: utf-8 -*-

import re

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        wds = f.read()
        return wds.split('\n')
    
    
def check(Line, countLine, start, end, k):
    flag = 0
    for i in range(countLine):
        if k == 0 and Line[i][0] == start and Line[i][1] == end:
            flag = 1
            break
        elif k > 0 and Line[i][0] == start and Line[i][1] != end:
            k -= 1
            flag = check(Line, countLine, Line[i][1], end, k)
            
    return flag
    
def writeFile(url, Line, countLine, Path, countPath):
    with open(url, 'w', encoding='utf8') as f:
        for i in range(countPath):
            # 起点, 终点, step=2
            # 两个顶点间 存在 长度为k的路径
            if check(Line, countLine, Path[i][0], Path[i][1], Path[i][2]):
                f.write('[{0}, {1}, YES]\n'.format(Path[i][0], Path[i][1]))
            else:
                f.write('[{0}, {1}, NO]\n'.format(Path[i][0], Path[i][1]))
                
def main():
    dataLine = readFile('./file/file_2013_PathInput.txt')
    dataPath = readFile('./file/file_2013_PathRequest.txt')
    
    countLine, countPath = int(dataLine[0]), int(dataPath[0])

    
    Line, Path = [], []
    for i in range(1, countLine + 1):
        A, B = re.findall('[A-Z]+', dataLine[i])
        Line.append([A, B])

        
    for i in range(1, countPath + 1):
        A, B = re.findall('[A-Z]+', dataPath[i])
        step = int(re.findall('[0-9]+', dataPath[i])[0])
        Path.append([A, B, step])

    print(dataLine, dataPath)
    print(Line)
    print(Path)
    
    writeFile('./file/file_2013_output.txt', Line, countLine, Path, countPath)
    
        
if __name__=='__main__':
    main()
    
    
    
    
    
    
"""
英文文本文件，读取内容将大写小写转换。
"""

def readwords(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    print('已读取' + filename)
    return lines

def switch(lines):
    for index, line in enumerate(lines):
        lines[index] = ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in line])
    print('已转换大小写')
    return lines

def writewords(filename, lines):
    f = open(filename, 'w')
    for line in lines:
        f.write(line)
    print('已写入' + filename)
    f.close()

if __name__ == "__main__":
    filename = './习题1.txt'
    writewords(filename, switch(readwords(filename)))
    
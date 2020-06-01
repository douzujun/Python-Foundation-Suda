"""
有一个 100G 的文件 largefile.txt（这个文件目前没有
100G，只是做模拟）。
实现一个程序，首先输出 largefile.txt 的行数，然后
无限循环，每次要求用户键盘输入一个行号，然后立刻输出对应行的文本。
由于文件很大，不允许将文件内容全部放到内存中； 
同时也不允许从头扫描文件，得到对应行的文本，因为这样速度太慢。
（提示：用二进制模式打开文件，使用 tell, seek 等方法）
"""

def read_in_block(file_path=r'Data\01_data.txt'):
    block_size = 16
    with open(file_path, 'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return

def count_line(file_generator):
    line_dict = {1:0}
    line = 1
    location = 0
    for block in file_generator:
        temp = 0
        for bytech in block:
            if bytech == 10:
                line += 1
                line_dict[line] = location+temp+1
            temp += 1
        location += 16
    return line, line_dict

def read_location(line, line_dict, file_path=r'Data\01_data.txt'):
    f = open(file_path, 'r')
    f.seek(line_dict[line])
    string = f.readline()
    print(string)
    f.close()

if __name__ == "__main__":
    file_generator = read_in_block()
    l,ld = count_line(file_generator)
    print("共{}行".format(l))
    while True:
        try:
            line = int(input("输入行号"))
            read_location(line, ld)
        except Exception as e:
            print(e)

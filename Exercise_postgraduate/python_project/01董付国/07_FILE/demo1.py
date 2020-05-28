if __name__ == '__main__':
    # 读取数据
    filename = 'demo1.py'
    with open(filename, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    # 调整数据

    # 未对齐
    data1 = []
    i = 1
    for line in lines:
        data1.append(line.rstrip() + '    # ' + str(i) + '\n')
        i += 1

    # 对齐方式1  str.ljust + rstrip()
    data2 = []
    max_len = max([len(line) for line in lines])
    i = 1
    for line in lines:
        data2.append('{0}{1}\n'.format(line.rstrip().ljust(max_len, ' ') + '# ', str(i)))
        i += 1
    # 对齐方式2
    data3 = [line.rstrip()+' '*(100-len(line))+'#'+str(index)+'\n' for index,line in enumerate(lines)]

    # 写入文件
    fp = open(filename[:-3] + '_new.py', 'a+')
    # 使用writelines
    fp.writelines(data2)
    # 使用print输入到文件中
    for line in data3:
        print(line, file=fp, end='')
    fp.close()

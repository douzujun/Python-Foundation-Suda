if __name__ == '__main__':    # 1
    # 读取数据    # 2
    filename = 'demo1.py'    # 3
    with open(filename, 'r', encoding='utf-8') as fp:    # 4
        lines = fp.readlines()    # 5
    # 调整数据    # 6
    # 7
    # 未对齐    # 8
    data1 = []    # 9
    i = 1    # 10
    for line in lines:    # 11
        data1.append(line.rstrip() + '    # ' + str(i) + '\n')    # 12
        i += 1    # 13
    # 14
    # 对齐方式1  str.ljust + rstrip()    # 15
    data2 = []    # 16
    max_len = max([len(line) for line in lines])    # 17
    i = 1    # 18
    for line in lines:    # 19
        data2.append('{0}{1}\n'.format(line.rstrip().ljust(max_len, ' ') + '# ', str(i)))    # 20
        i += 1    # 21
    # 22
    # 写入文件    # 23
    fp = open(filename[:-3] + '_new.py', 'a+')    # 24
    # 使用writelines    # 25
    fp.writelines(data1)    # 26
    # 使用print输入到文件中    # 27
    for line in data2:    # 28
        print(line, file=fp, end='')    # 29
    fp.close()    # 30
if __name__ == '__main__':                                                                # 1
    # 读取数据                                                                                # 2
    filename = 'demo1.py'                                                                 # 3
    with open(filename, 'r', encoding='utf-8') as fp:                                     # 4
        lines = fp.readlines()                                                            # 5
    # 调整数据                                                                                # 6
                                                                                          # 7
    # 未对齐                                                                                 # 8
    data1 = []                                                                            # 9
    i = 1                                                                                 # 10
    for line in lines:                                                                    # 11
        data1.append(line.rstrip() + '    # ' + str(i) + '\n')                            # 12
        i += 1                                                                            # 13
                                                                                          # 14
    # 对齐方式1  str.ljust + rstrip()                                                         # 15
    data2 = []                                                                            # 16
    max_len = max([len(line) for line in lines])                                          # 17
    i = 1                                                                                 # 18
    for line in lines:                                                                    # 19
        data2.append('{0}{1}\n'.format(line.rstrip().ljust(max_len, ' ') + '# ', str(i))) # 20
        i += 1                                                                            # 21
                                                                                          # 22
    # 写入文件                                                                                # 23
    fp = open(filename[:-3] + '_new.py', 'a+')                                            # 24
    # 使用writelines                                                                        # 25
    fp.writelines(data1)                                                                  # 26
    # 使用print输入到文件中                                                                       # 27
    for line in data2:                                                                    # 28
        print(line, file=fp, end='')                                                      # 29
    fp.close()                                                                            # 30
if __name__ == '__main__':                                                                             # 1
    # 读取数据                                                                                             # 2
    filename = 'demo1.py'                                                                              # 3
    with open(filename, 'r', encoding='utf-8') as fp:                                                  # 4
        lines = fp.readlines()                                                                         # 5
    # 调整数据                                                                                             # 6
                                                                                                       # 7
    # 未对齐                                                                                              # 8
    data1 = []                                                                                         # 9
    i = 1                                                                                              # 10
    for line in lines:                                                                                 # 11
        data1.append(line.rstrip() + '    # ' + str(i) + '\n')                                         # 12
        i += 1                                                                                         # 13
                                                                                                       # 14
    # 对齐方式1  str.ljust + rstrip()                                                                      # 15
    data2 = []                                                                                         # 16
    max_len = max([len(line) for line in lines])                                                       # 17
    i = 1                                                                                              # 18
    for line in lines:                                                                                 # 19
        data2.append('{0}{1}\n'.format(line.rstrip().ljust(max_len, ' ') + '# ', str(i)))              # 20
        i += 1                                                                                         # 21
    # 对齐方式2                                                                                            # 22
    data3 = [line.rstrip()+' '*(100-len(line))+'#'+str(index)+'\n' for index,line in enumerate(lines)] # 23
                                                                                                       # 24
    # 写入文件                                                                                             # 25
    fp = open(filename[:-3] + '_new.py', 'a+')                                                         # 26
    # 使用writelines                                                                                     # 27
    fp.writelines(data2)                                                                               # 28
    # 使用print输入到文件中                                                                                    # 29
    for line in data3:                                                                                 # 30
        print(line, file=fp, end='')                                                                   # 31
    fp.close()                                                                                         # 32
if __name__ == '__main__':                                                                         #0
    # 读取数据                                                                                         #1
    filename = 'demo1.py'                                                                          #2
    with open(filename, 'r', encoding='utf-8') as fp:                                              #3
        lines = fp.readlines()                                                                     #4
    # 调整数据                                                                                         #5
                                                                                                   #6
    # 未对齐                                                                                          #7
    data1 = []                                                                                     #8
    i = 1                                                                                          #9
    for line in lines:                                                                             #10
        data1.append(line.rstrip() + '    # ' + str(i) + '\n')                                     #11
        i += 1                                                                                     #12
                                                                                                   #13
    # 对齐方式1  str.ljust + rstrip()                                                                  #14
    data2 = []                                                                                     #15
    max_len = max([len(line) for line in lines])                                                   #16
    i = 1                                                                                          #17
    for line in lines:                                                                             #18
        data2.append('{0}{1}\n'.format(line.rstrip().ljust(max_len, ' ') + '# ', str(i)))          #19
        i += 1                                                                                     #20
    # 对齐方式2                                                                                        #21
    data3 = [line.rstrip()+' '*(100-len(line))+'#'+str(index)+'\n' for index,line in enumerate(lines)]#22
                                                                                                   #23
    # 写入文件                                                                                         #24
    fp = open(filename[:-3] + '_new.py', 'a+')                                                     #25
    # 使用writelines                                                                                 #26
    fp.writelines(data2)                                                                           #27
    # 使用print输入到文件中                                                                                #28
    for line in data3:                                                                             #29
        print(line, file=fp, end='')                                                               #30
    fp.close()                                                                                     #31

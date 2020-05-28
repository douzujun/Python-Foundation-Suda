# -*- coding: utf-8 -*-

import re

def solve():
    while True:
        line = input()
        if line == '#':
            break
        num = re.findall('[0-9]+', line)
        if num:
            line = line.split()
            pwd, cnt = line[0], int(line[1])
            for i in range(cnt):
                test = input()
                if test == pwd:
                    print('Welcome in')
                    break
                elif test != pwd:
                    print('Wrong password: {0}'.format(test))
            else:
                print('Account locked')
      
      
solve()
            
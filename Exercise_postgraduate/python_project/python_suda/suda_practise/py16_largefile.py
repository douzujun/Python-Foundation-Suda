# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:51:38 2020

@author: douzi
"""

def readFile(url):
    with open(url, 'rb') as f:
        print("行号", len(f.readlines()))
        while True:
            line = ''
            f.seek(0)
            cur = 0
            n = int(input("input: "))
            while cur < n - 1:
                f.readline()
                cur += 1
            line = f.readline()
            if not line:
                break
            else:
                print(line)
            
def readFile1(url):
    count = 1
    with open(url, 'rb') as f:
        while True:
            buff = f.read(8192*1025)
            buff = buff.decode('utf8')
            print(buff)
            count += buff.count('\n')
            if not buff:
                break
    print(count)
        
def main():
    readFile('./file/file15_largefile.txt')
    
    readFile1('./file/file15_largefile.txt')

if __name__=='__main__':
    main()
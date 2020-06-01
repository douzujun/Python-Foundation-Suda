# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:34:25 2020

@author: douzi
"""
import os

def copy(url):
    with open(url, 'r', encoding='utf8') as f:
        data = f.read()
    
    outfile = os.path.join(os.path.dirname(url), 'file12_new.txt')
    print(outfile)
    
    with open(outfile, 'w', encoding='utf8') as f:
        f.write(data)
        

def main():
    copy('./file/file12_copy.txt')
    
if __name__=='__main__':
    main()
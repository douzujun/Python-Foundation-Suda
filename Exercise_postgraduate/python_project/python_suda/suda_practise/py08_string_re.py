# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:11:49 2020

@author: douzi
"""

def recombine(s):
    if len(s) < 2:
        return ""
    return s[0:2] + s[-2:]

def main():
    print(recombine('python'))
    print(recombine('py'))
    print(recombine('d'))
    
    
if __name__=='__main__':
    main()
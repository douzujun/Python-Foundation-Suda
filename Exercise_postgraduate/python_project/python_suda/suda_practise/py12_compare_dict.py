# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 18:14:56 2020

@author: douzi
"""

def compare(dict1 : dict, dict2 : dict):
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            if key1 == key2:
                return key1


def main():
    dict1 = {1:'a', 2:'b', 3:'c'}
    dict2 = {1:'A', (2,3):'B', '4':'C'}
    a = compare(dict1, dict2)
    print(a)
    
if __name__=='__main__':
    main()
    
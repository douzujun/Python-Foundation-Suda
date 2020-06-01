# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:42:28 2020

@author: douzi
"""

def fun5(str1):
    li = list(str1)
    print(li)
    
    res = []
    for elem in li:
        if elem == '(':
            res.append(elem)
        elif elem == '{':
            res.append(elem)
        elif elem == '[':
            res.append(elem)
        elif elem == ')':
            if len(res) >= 1:
                t = res.pop()
                if t != '(':
                    return False
            else:
                return False
        elif elem == ']':
            if len(res) >= 1:
                t = res.pop()
                if t != '[':
                    return False
            else:
                return False
        elif elem == '}':
            if len(res) >= 1:
                t = res.pop()
                if t != '{':
                    return False
            else:
                return False
   
    return True
    
    
def main():
    print(fun5('(())'))
    print(fun5('(()]'))
    print(fun5('({})'))
    print(fun5('[{()}]'))
    print(fun5('([)'))
    print(fun5('][]'))
    
main()
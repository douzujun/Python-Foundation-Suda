# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:10:01 2020

@author: douzi
"""

def plural(s):
    s = list(s)
    if s[-1] == 'y':
        del s[-1]
        s.append('ies')
    elif s[-1] in ['o', 's', 'x', 'z']:
        s.append('es')
    elif s[-2]+s[-1] in ['sh', 'ch']:
        s.append('es')
    else:
        s.append('s')
        
    return "".join(s)
        
def main():
    print(plural('fly'))
    print(plural('hero'))
    print(plural('bitch'))
    print(plural('bash'))
    print(plural('hex'))
    print(plural('girl'))


if __name__=='__main__':
    main()
    